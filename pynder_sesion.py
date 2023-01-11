import time
import pynder

def main():
    
    session = pynder.Session(FACEBOOK_ID, USER_TOKEN)
    session.update_location('LAT', 'LON') # updates latitude and longitude for your profile
    session.profile  # your profile. 
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
