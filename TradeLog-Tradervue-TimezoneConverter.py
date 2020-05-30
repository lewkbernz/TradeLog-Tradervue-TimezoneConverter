import datetime
import os
import pytz
import pandas as pd


def main():

    CITY_TO = ""
    CITY_FROM = ""
    FMT = "%Y%m%d %H:%M:%S"

    try:

        INPUT_TO = input("\nWhat city or timezone do you want to convert TO [default: New York]? ") or "New York"
        INPUT_TO = INPUT_TO.replace(' ','_')
    
        for ALLZONES in filter(lambda x: INPUT_TO.title() in x, pytz.all_timezones):
            CITY_TO = ALLZONES

        if CITY_TO:
            print("\nThe current date and time in " + CITY_TO + " is: " + str(datetime.datetime.now(pytz.timezone(CITY_TO))) + ".\nIf the timezone is incorrect, hit CTRL+C and check the timezone list.")
            pass
        else:
            raise Exception("\nCannot find the TO timezone. Maybe try another city nearby?\n")

        INPUT_FROM = input("\nWhat city or timezone do you want to convert FROM [default: Sydney]? ") or "Sydney"
        INPUT_FROM = INPUT_FROM.replace(' ','_')

        for ALLZONES in filter (lambda x: INPUT_FROM.title() in x, pytz.all_timezones):
            CITY_FROM = ALLZONES

        if CITY_FROM:
            print("\nThe current date and time in " + CITY_FROM + " is: " + str(datetime.datetime.now(pytz.timezone(CITY_TO))) + ".\nIf the timezone is incorrect, hit CTRL+C and check the timezone list.")
            pass
        else:
            raise Exception("\nCannot find the FROM timezone. Maybe try another city nearby?\n")

        TZ_TO = pytz.timezone(CITY_TO)
        DT_TO = datetime.datetime.now(TZ_TO)
        TZ_FROM = pytz.timezone(CITY_FROM)
        DT_FROM = datetime.datetime.now(TZ_FROM)
        
        DTDELTA = DT_FROM.replace(tzinfo=None) - DT_TO.replace(tzinfo=None)
        TIMEDIFF = (DTDELTA).total_seconds() / 3600

        if TIMEDIFF < 0:
            print("\n" + CITY_TO + " is " + str('%.2f' % abs(TIMEDIFF)) + " hours AHEAD of " + CITY_FROM + "\n")
        elif TIMEDIFF > 0:
            print("\n" + CITY_TO + " is " + str('%.2f' % abs(TIMEDIFF)) + " hours BEHIND of " + CITY_FROM + "\n")
        else:
            print("\nThere is no time difference between " + CITY_TO + " and " + CITY_FROM + ".\n")
            print("No time conversion necessary.\n")
            input("Press enter to exit")
            exit()

        try:

                BUFFER = []
                START = "STK_TRD"
                OUTPUT = ""
                INPUT = ""

                INPUT = input("Input file [default: input.tlg]? ") or "input.tlg"

                try:
                    for INPUT_LINE in open(INPUT):
                        if INPUT_LINE.startswith(START):
                            BUFFER.append(INPUT_LINE)

                except:
                    print("\nCannot open input file! Check it exists and is readable\n")
                    input("Press enter to try again")
                    main()
        
                OUTPUT = input("Output file [default: output.txt]? ") or "output.txt"
                EXPORT = open(OUTPUT,'w')
                
                for BUFFER_LINE in BUFFER:
                        TRADE_LIST = BUFFER_LINE.split("|")
                        indtg = datetime.datetime.strptime(TRADE_LIST[7] + " " + TRADE_LIST[8], FMT)
                        outdtg = TZ_FROM.localize(indtg)
                        newdtg = (TZ_TO.normalize(outdtg).strftime(FMT))
                        TRADE_LIST[7] = newdtg.split(" ")[0]
                        TRADE_LIST[8] = newdtg.split(" ")[1]
                        EXPORT.write("|".join(TRADE_LIST))
        except KeyboardInterrupt:
                raise Exception
        
        except Exception as e:
                print("\nERROR: " + e + "\n")
                input("Press any key to try again")
                main()

        print ("\nFinished!")
        print(("Import the " + OUTPUT + " file into Tradervue\n"))
        input("Press enter to exit")
        exit()

    except KeyboardInterrupt:
        FAIL = input("Would you like to see a full list of city timezones [y/N]? ") or "n"
        FAIL = FAIL.lower()
        if FAIL == 'y' or FAIL == 'yes':
            for TIMEZONE in pytz.all_timezones:
                print(TIMEZONE)
        main()

    except Exception:
        try:
            FAIL = input("Would you like to see a full list of city timezones [y/N]? ") or "n"
            FAIL = FAIL.lower()
            if FAIL == 'y' or FAIL == 'yes':
                for TIMEZONE in pytz.all_timezones:
                    print(TIMEZONE)
                main()
            else:
                main()
        except:
            exit()

main()


	
	
