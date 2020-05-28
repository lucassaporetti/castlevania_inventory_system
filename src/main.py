#!/usr/bin/env python

"""
  @package: TODO describe
   @script: ${app.py}
  @purpose: ${purpose}
  @created: MAY 28, 2020
   @author: Lucas Saporetti
   @mailto: lucassaporetti@gmail.com
"""

import signal
import sys

if len(sys.argv) > 1 and sys.argv[1].upper() == 'QT':
    from src.ui.qt.castlevania_inventory_qt import CastlevaniaInventoryQt


def exit_app(sig=None, frame=None):
    print(frame)
    print('\033[2J\033[H')
    print('Bye.')
    print('')
    exit(sig)


# Application entry point
if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_app)
    CastlevaniaInventoryQt().run()
    exit_app(0)
