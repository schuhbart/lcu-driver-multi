import asyncio
import logging
from abc import ABC
from sys import platform
from typing import Union

from psutil import Process

from .connection import Connection
from .events.managers import ConnectorEventManager, WebsocketEventManager
from .utils import _return_ux_process_when_available

logger = logging.getLogger('lcu-driver')


class BaseConnector(ConnectorEventManager):
    def __init__(self, loop=None):
        super().__init__()
        self.loop = loop
        self.ws = WebsocketEventManager()
        self.connection = None

    def create_connection(self, process_or_string: Union[Process, str], name=""):
        """Creates a connection and saves a reference to it"""
        connection = Connection(self, process_or_string, name=name, loop=self.loop)
        self.connection = connection

    def remove_connection(self):
        """Cancel the connection"""
        self.connection = None


class Connector(BaseConnector):
    def __init__(self, *, name="", loop=None):
        super().__init__(loop)
        self._repeat_flag = True
        self.name = name
        self.started = False

    def is_started(self):
        return self.started

    def start(self) -> bool:
        """Starts the connector. This method should be overridden if different behavior is required.

        :rtype: None
        """
        try:
            def wrapper():
                connections = _return_ux_process_when_available()
                for connection in connections:
                    self.create_connection(connection, name=self.name)
                    req = self.connection.request_sync("get", '/lol-chat/v1/me')
                    if req:
                        if req['gameName'].lower() == self.name.lower() or self.name == "":
                            # this fires the @connector.ready event
                            self.started = True
                            if self.loop:
                                self.loop.create_task(self.connection.init())
                            else:
                                asyncio.get_event_loop().run_until_complete(self.connection.init())
                            return True

                print(f"Error: did not find client matching name {self.name}.")
                return False


            return wrapper()
        except KeyboardInterrupt:
            logger.info('Event loop interrupted by keyboard')

    async def stop(self) -> None:
        """Flag the connector to don't look for more clients once the connection finishes his job.

        :rtype: None
        """
        self._repeat_flag = False
