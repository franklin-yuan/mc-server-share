@echo off
REM Add custom JVM arguments (such as RAM allocation) to the user_jvm_args.txt

java -Xmx8192M -Xms8192M -jar forge.jar nogui

pause


