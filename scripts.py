from manage_db import SocialDB
import time

def populateUsers(db):
    db.addPerson("Hank Hill", "hank1")
    db.addPerson("Sam Doe", "samwich")
    db.addPerson("Sho Gun", "Shogun")
    db.addPerson("Jane Doe", "The Soldier")
    db.addPerson("Todd Howard", "Bethesda")
    db.addPerson("Anna", "aplpaca")

def populateFollow(db):
    db.following("hank1", "aplpaca")
    db.following("samwich", "aplpaca")
    db.following("Shogun", "aplpaca")
    db.following("The Soldier", "aplpaca")
    db.following("Bethesda", "aplpaca")
    db.following("Shogun", "Bethesda")
    db.following("The Soldier", "Bethesda")
    db.following("The Soldier", "Shogun")
    db.following("hank1", "samwich")
    db.following("Shogun", "samwich")

def makePost(db):
    db.addPost("aplpaca", "birds are cool") #1
    time.sleep(1)
    db.addPost("aplpaca", "cats are cool") #2
    time.sleep(1)
    db.addPost("aplpaca", "dogs are cool") #3
    time.sleep(1)
    db.addPost("aplpaca", "dinosaurs are cool") #4
    time.sleep(1)
    db.addPost("aplpaca", "bats are cool") #5
    time.sleep(1)
    db.addPost("aplpaca", "bugs are cool") #6
    time.sleep(1)
    db.addPost("Bethesda", "it just works") #7
    time.sleep(1)
    db.addPost("The Soldier", '"If fighting were to result in victory then you must fight" ~Sun Tzu') #8
    time.sleep(1)
    db.addPost("Shogun", "First name Sho last name Gun") #9
    time.sleep(1)
    db.addPost("Shogun", "Why didn't anyone warn me that becoming a robotics engineer would require math") #10
    time.sleep(1)
    db.addPost("The Soldier", "Godspeed, you magnificent bastard.") #11
    time.sleep(1)
    db.addPost("hank1", "Propane and propane accessories") #12
    time.sleep(1)
    db.addPost("samwich", "My name is samwich") #13
    time.sleep(1)
    db.addPost("Bethesda", "Buy Skyrim again") #14

def makeComment(db):
    db.comment("hank1", 2, "I prefer dogs") #1
    db.comment("Shogun", 2, "yeah") #2
    db.comment("hank1", 1, "yeah") #3
    db.comment("Shogun", 7, "It does not") #4
    db.comment("aplpaca", 10, "Loser") #5
    db.comment("aplpaca", 13, "that's a good name") #6

def likePost(db):
    db.like("Shogun", 2)
    db.like("Shogun", 1)
    db.like("Shogun", 3)
    db.like("Shogun", 4)
    db.like("Shogun", 5)
    db.like("Shogun", 6)
    db.like("The Soldier", 7)
    db.like("The Soldier", 12)
    db.like("aplpaca", 9)
    db.like("aplpaca", 10)

def makeReply(db):
    db.reply("aplpaca", 2, 1, "make your own post") #7
    db.reply("hank1", 2, 7, "Fine") #8
    db.reply("Bethesda", 7, 4, "Trust me") #9
    db.reply("samwich", 13, 6, "Thanks :)") #10
    db.reply("Shogun", 10, 5, ":(") #11

def main():
    print("If the program seems slow, don't worry, I set up built in delays or else the demonstration of the feed would fail as all posts would share the same date and time")
    db = SocialDB()
    populateUsers(db)
    populateFollow(db)
    makePost(db)
    makeComment(db)
    likePost(db)
    makeReply(db)
    print("FEED: ", db.getFeed("Shogun", 20))
    print("COMMENTS: ", db.getComments(2))
    print("CIRCLES: ", db.circles("The Soldier", 4))

if __name__ == "__main__":
    main()
