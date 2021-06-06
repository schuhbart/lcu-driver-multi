from typing import Dict, List, Optional

from psutil import process_iter, Process


def parse_cmdline_args(cmdline_args) -> Dict[str, str]:
    cmdline_args_parsed = {}
    for cmdline_arg in cmdline_args:
        if len(cmdline_arg) > 0 and '=' in cmdline_arg:
            key, value = cmdline_arg[2:].split('=')
            cmdline_args_parsed[key] = value
    return cmdline_args_parsed


def return_process(process_name: List[str]):
    processes = []
    for process in process_iter():
        if process.name() in process_name:
            processes.append(process)
    return processes


def _return_ux_process_when_available():
    processes = return_process(['LeagueClientUx.exe', 'LeagueClientUx'])
    return processes
