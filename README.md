# lcu-driver-multi

A fork from [lcu_driver](https://github.com/sousa-andre/lcu-driver) that supports running multiple clients at the same time. 

## "Installation"
To use the library, clone the repo and import it. 

## Documentation
The original lcu_driver documentation is [here](https://lcu-driver.readthedocs.io/)
This fork should be mostly backwards compatible. It adds a few features to make the library usable with multiple clients:

  - passing a name to the connector constructor will make it only connect to a client that is logged in with that name (case insensitive)
  - connector.start() returns True if a client with the specified name was found, or False otherwise
  - if an event loop is passed to the connector constructor, connector.start() will **NOT** block the entire program anymore. Instead the event listeners are added to the passed event loop
  - the name and event loop are accessible from inside of the connection object to allow for easy reconstruction of the connector if the client is closed and reopened

Also included is a synchronous get / post method. It was required for making the connector name parameter work, so it's there. If you don't feel like figuring out Python's asyncio then I suppose you could use that instead, but I would not recommend it.

The repository contains the lcu_tools.py example file that should demonstrate every new feature. It also includes a few other random functions and the amogus potion copypasta, free of charge.

## Endorsement
lcu-driver-multi isn’t endorsed by Riot Games and doesn’t reflect the views or opinions of Riot Games or anyone officially involved in producing or managing League of Legends. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.
