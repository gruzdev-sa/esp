#!/usr/bin/env python3

# Copyright (c) 2011-2021 Columbia University, System Level Design Group
# SPDX-License-Identifier: Apache-2.0

###############################################################################
#
# ESP Wrapper Generator for Accelerators
#
###############################################################################

import sys

from tkinter import *
from tkinter import messagebox
from soc import *
from socmap_gen import *
from mmi64_gen import *
from power_gen import *

def print_usage():
  print("Usage                    : ./esp_creator.py <dma_width> <tech> <MAC>")
  print("")
  print("")
  print("      <dma_width>        : Bit-width for the DMA channel (currently supporting 32 bits only)")
  print("      <tech>             : Target technology (e.g. virtex7, virtexu, virtexup, ...)")
  print("      <MAC>              : MAC Address for Linux network interface)")
  print("      <LEON3_STACK>      : Stack Pointer for LEON3)")
  print("")

if len(sys.argv) != 5:
    print_usage()
    sys.exit(1)

DMA_WIDTH = int(sys.argv[1])
TECH = sys.argv[2]
LINUX_MAC = sys.argv[3]
LEON3_STACK = sys.argv[4]

root = Tk()
soc = SoC_Config(DMA_WIDTH, TECH, LINUX_MAC, LEON3_STACK, False)

esp_config = soc_config(soc)
create_socmap(esp_config, soc)
create_power(soc)
create_mmi64_regs(soc)

