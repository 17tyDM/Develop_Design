import sys
def test_command():
	args = sys.argv
	print(args[0])# ←「test_command.py」が出力
	print(args[1])# ←「a」が出力
	print(args[2])# ←「b」が出力

test_command()