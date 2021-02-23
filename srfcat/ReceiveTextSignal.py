#!/usr/bin/env python

from rflib import *


class ReceiveSignal:

    __SIGNAL_SETTINGS = {"frequency": 434000000,
                         "baud_rate": 4800,
                         "modulation": "ASK/OOK",
                         "lowball": False,
                         "max_power": False}

    def __init__(self):
        pass

    @staticmethod
    def __verify_range(value, minimum, maximum):
        """
        verify frequency inside given range

        :type value: int
        :param value: value of frequency to verify
        :type minimum: int
        :param minimum: minimum value to verify
        :type maximum: int
        :param maximum: maximum value to verify

        :return: bool
        """
        if value in range(minimum, maximum):
            return True
        else:
            return False

    @staticmethod
    def set_frequency(value):
        """
        set frequency in MHz

        :type value: int
        :param value: integer in MHz
        """
        min_yst = 300000000
        max_yst = 928000000
        checklist = [int(value), min_yst, max_yst]

        if ReceiveSignal.__verify_range(*checklist):
            ReceiveSignal.__SIGNAL_SETTINGS['frequency'] = int(value)
        else:
            sys.stdout.write("Error {} not between {} and {}".format(*checklist))
            sys.exit(2)

    @staticmethod
    def set_baud_rate(value):
        """
        set baud rate in MHz

        :type value: int
        :param value: integer in MHz
        """
        min_yst = 210
        max_yst = 250000
        checklist = [int(value), min_yst, max_yst]

        if ReceiveSignal.__verify_range(*checklist):
            ReceiveSignal.__SIGNAL_SETTINGS['baud_rate'] = int(value)
        else:
            sys.stdout.write("Error: baud rate {} not between {} and {}".format(*checklist))
            sys.exit(2)

    @staticmethod
    def set_lowball(value):
        """
        set lowball

        :type value: bool
        :param value: true or false
        """

        ReceiveSignal.__SIGNAL_SETTINGS['lowball'] = bool(value)

    @staticmethod
    def set_max_power(value):
        """
        set max power

        :type value: bool
        :param value: true or false
        """

        ReceiveSignal.__SIGNAL_SETTINGS['max_power'] = bool(value)

    @staticmethod
    def get_signal_dump():
        """
        dump signal information to STDOUT
        """
        divider = '-' * 80

        print("SIGNAL RECEIVE INFORMATION")
        print(divider)
        print('Frequency in MHz : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['frequency']))
        print('Baud rate in MHz : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['baud_rate']))
        print('Modulation       : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['modulation']))
        print('LOWBALL          : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['lowball']))
        print('MAX POWER        : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['max_power']))
        print(divider)

    @staticmethod
    def get_signal():
        """
        receive signal with rfcat
        """
        rfc_obj = RfCat()
        # @ToDo: create set method for modulation
        rfc_obj.setMdmModulation(MOD_ASK_OOK)
        rfc_obj.setFreq(ReceiveSignal.__SIGNAL_SETTINGS['frequency'])
        rfc_obj.setMdmDRate(ReceiveSignal.__SIGNAL_SETTINGS['baud_rate'])
        if ReceiveSignal.__SIGNAL_SETTINGS['lowball']:
            rfc_obj.lowball()
        if ReceiveSignal.__SIGNAL_SETTINGS['max_power']:
            rfc_obj.setMaxPower()
        rfc_obj.lowball()
        rfc_obj.RFlisten()
        rfc_obj.setModeIDLE()
