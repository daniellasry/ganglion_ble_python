from ganglion_ble import Ganglion

board = Ganglion(port='COM6', mac_addrs='E65D54F2F438')
board.connect()
print('connected')
board.send_board_command('[')
# board.set_channels([1, 0, 0, 1])
board.send_board_command('b')
board.start_stream()
# time.sleep(1)
# board.disconnect()
