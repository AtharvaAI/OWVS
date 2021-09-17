import subprocess
import json

def run_tool_command(tool, command):
	print("Starting process {}".format(tool))

	process = subprocess.run(
		command,
		capture_output=True,
		universal_newlines=True,
		timeout=None,
		shell=True
	)

	if process.returncode == 0:
		print("Ending process")
		return True, process
	else:
		print("Failed process")
		print(process.stderr)
		return False, process