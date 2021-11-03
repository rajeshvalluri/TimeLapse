#All credit goes to the original authors
import RPi.GPIO as GPIO
import time

print '\nWelcome to the Complete Manual Time-lapse Tool.'
print '\nPlease answer the following questions to get started.'
print '\nHow many shots in total and how  long between shots?'

def main():
        shots = raw_input('Number of shots you want to take?\n')
        interval = raw_input('\nHow frequently do you want these pictures(in Seconds)?\n')
#Cast the inputs into integers
        if shots.isdigit() and interval.isdigit():
                shots = int(shots)
                interval = int(interval)
                print('It will take %d minutes to complete the process.\n'%(shots*interval/60))
                answer = raw_input('Are you ready to proceed?(yes or no)\n')
                confirm = answer.lower() in ['yes','no']
                if confirm:
                    GPIO.setmode(GPIO.BOARD)
                    GPIO.setup(16,GPIO.OUT)
                    taken = 1
                    print
                    print 'Starting a run of %d shots'% (shots)
                    for cnt in range(0,shots):
                        print
                        print( 'Shot %d of %d' % (taken, shots))
                        taken += 1
                        GPIO.output(16,GPIO.HIGH)
                        time.sleep(0.5)
                        GPIO.output(16,GPIO.LOW)
                        time.sleep(interval)
                    GPIO.cleanup()
                else:
                    print 'Please try again with the right inputs\n'
                    main()
        else:
            print '\nUser input Error. Please enter numbers only. Try again\n'
            main()
        print 'Thanks for using the Timelapse Tool'
        print 'Would you like to go again\n'
        again = raw_input('Yes or No\n')
        proceed = again.lower() in ['yes','y']
        if proceed:
            main()
        else:
            print 'See you next time.'
            quit()
if __name__ == '__main__':
        main()
~                
