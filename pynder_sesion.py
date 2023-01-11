import time
import pynder

def main():
    
    session = pynder.Session(100089023886773, 'EAANWMpZCat44BAGo4bcZAKvHOMawSxlPBa9Q1afjYIBELX62N2iFnstZC0KNaZC7YtGLupKzS3ugM2dTBmgLJbsEug63ooRGoZATKp95lgw4P6PsBdavbSp1Ymhr43TvrXW0a2E4YN4g0pmtUVfxe4EiCT8J7biZCcfH0sRq1vVZBZBsM5TvyErQi9RhMpNsuDMZD')
    session.update_location('40.416775', '-3.703790') # updates latitude and longitude for your profile
    session.profile  # your profile. If you update its attributes they will be updated on Tinder.
    users = session.nearby_users() # returns a list of users nearby
    
    
    for user_name, user_id in users:
        print('Swiping right on', user_name)
        session.swipe_right(user_id)
        time.sleep(1)
        
    match_queue = session.matches() # get users you have already been matched with
    message = "Will you be my valentine?"
    for user_name, uid in match_queue:
        print('Messaging', user_name)
        send_message(message)
        time.sleep(1)    



if __name__ == "__main__":
    main()
