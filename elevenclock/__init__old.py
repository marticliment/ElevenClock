try:
    from clocks import main
    print("Starting...")
    main()
except Exception as e:
    import webbrowser, traceback, platform
    os_info = f"" + \
        f"                        OS: {platform.system()}\n"+\
        f"                   Release: {platform.release()}\n"+\
        f"           OS Architecture: {platform.machine()}\n"+\
        f"          APP Architecture: {platform.architecture()[0]}\n"+\
        f"                   Program: ElevenClock"+\
        "\n\n-----------------------------------------------------------------------------------------"
    traceback_info = "Traceback (most recent call last):\n"
    try:
        for line in traceback.extract_tb(e.__traceback__).format():
            traceback_info += line
        traceback_info += f"\n{type(e).__name__}: {str(e)}"
    except:
        traceback_info += "\nUnable to get traceback"
    traceback_info += str(type(e))
    traceback_info += ": "
    traceback_info += str(e)
    webbrowser.open("https://www.somepythonthings.tk/error-report/?appName=ElevenClock&errorBody="+os_info.replace('\n', '{l}').replace(' ', '{s}')+"{l}{l}{l}{l}ElevenClock Log:{l}"+str("\n\n\n\n"+traceback_info).replace('\n', '{l}').replace(' ', '{s}'))
    raise e