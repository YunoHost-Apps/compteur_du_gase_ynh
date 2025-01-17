#!/bin/bash

#=================================================
# COMMON VARIABLES AND CUSTOM HELPERS
#=================================================

_venv_install() {
    ynh_exec_as_app python3 -m venv --upgrade "$install_dir/venv"
    venvpy="$install_dir/venv/bin/python3"

    ynh_exec_as_app "$venvpy" -m pip install --upgrade --no-cache-dir pip

    ynh_exec_as_app "$venvpy" -m pip install setuptools wheel pyyaml
}
