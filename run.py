""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy,smart_run

# login credentials
insta_username = ''  # <- enter username here
insta_password = ''  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username='mr_haseebi',
                  password='Bolakhan51',
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    # session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])
    session.set_do_follow(True,percentage=100)


    # activity
    session.like_by_tags(
        ['fitness', 'igfitness', 'fitnessplayground', 'gymlife', 'workingout', 'fitnesspeople', 'fitnessgoals', 'followfit', 'fithumans', 'fithour', 'fitnesstime', 'fitnesspowers', 'fitnesseducation', 'fitnessclassroom', 'fitnessofinstagram', 'fitnessbased', 'fitnessthatlives', 'workout', 'fitnessschool', 'fitnessfollow', 'gymnasium', 'fitnessisalifestyle', 'gymlife', 'workingout', 'fitnesspeople', 'fitnessgoals', 'followfit', 'fithumans', 'fithour', 'fitnesstime\n', '', '', '', '', '\n\n', '', '', '', 'fitfood', 'glutenfreefitness', 'healthyeating', 'healthyrecipes', 'fitnessnutrition', 'paleofitness', 'veganfitness', 'fitnessinstructor', 'fitnessknows', 'fitnessballroom', 'indoorfitness', 'fitnessittoday', 'fitnessglobal', 'fitnessexercise', 'fitnessyoga', 'calisthenics', 'physical', 'obesityends', 'fitnessrehearsal', 'fitnessexertion', 'sport', 'healthit', 'fitnessworks', 'immune', 'fitnesssystem', 'fitnesssweat', 'fitnweight', 'fitnesspage', 'muscleit', 'exercising\n\n', '', '', '', '', '\n\n', '', '', '', '', '\n\n', '', '', '', 'fitnessstretch', 'bodybuilding', 'gymnastic', 'fitnesseffort', 'fitnesstherapy', 'fitnessaerobic', 'physiotherapy', 'fitnesseverything', 'depressionends', 'callisthenics', 'jazzercise', 'fitnessjog', 'fitnessregimen', 'isometric', 'gym', 'fitnessseason', 'cardio', 'fitnessrehab', 'treadmill', 'fitnessroutines', 'fitnesstrain', 'training', 'fitnesssessions', 'fitnessdrills', 'fitnesstryout', 'fitnessfam', 'fitnesscheckup', 'minicamp', 'fitnesspractice', 'fitnesstilltheend\n\n', '', '', '', '', '\n\n', '', '', '', 'fitnesssleep', 'healthyfitness', 'set', 'stretching', 'workouts', 'accuracy', 'breathlessness', 'fitnessspeed', 'fitnessstrech', 'warmdown', 'systole', 'musclebuilding', 'isometrics', 'fitnessunderexercise', 'unexercised', 'nonjogging', 'exercisable', 'selfesteem', 'perspire', 'epidemiology', 'exergame', 'exergaming', 'perspiration', 'notiredness', 'diastole', 'fitnessexcersisethatwork', 'biomarker', 'fitnessroutine', 'fitnesslifestyle', 'physiotherapist\n\n', '', '', '', '', '\n\n', '', '', '', '', '\n\n', '', '', '', 'inflammation', 'grueling', 'healthiness', 'fitnessschedule', 'cardiovascular', 'fitnessfood', 'unsweat', 'rehearsals', 'sweatpants', 'regularfitness', 'regimens', 'shvitz', 'fitnessrefresher', 'debriefing', 'fitnesscoaching', 'fitnesslocker', 'fitnesspreparation', 'hidrosis', 'fitnesssweatsuit', 'lockers', 'clubhouse', 'fitnesstennis', 'rink', 'hallway', 'auditorium', 'bleachers', 'fitnessjogging', 'fitnessclasses', 'hall', 'basketball\n\n', '', '', '', '', '\n\n', '', '', '', '', '\n\n', '', '', '', 'fitnesssauna', 'athletics', 'fitnessgyms', 'fitnesslawn', 'fitnesshalls', 'fitnessrooms', 'outdoorfitness', 'tent', 'diningfitness', 'fitnesstolive', 'outdoorsfitnesspeople', 'dormitories', 'fitnessrestroom', 'fitnesssitting', 'upstairs', 'swimming', 'shower', 'fitnessdorms', 'classrooms', 'dormitory', 'sleeping', 'fitnesstoilet', 'parlor', 'sit', 'softball', 'kitchen', 'lounges', 'fitnessmassage', 'playgrounds', 'fitnessbackyard\n\n', '', '', '', '', '\n\n', '', '', '', '', '\n\n', '', '', '', 'sports', 'chair', 'fitnessshoes', 'fitnessstream', 'fitnessfan', 'buddies', 'fitnesswear', 'fitnesssat', 'walking', 'parking', 'fitnessprep', 'fitnessgarage', 'lounging', 'sweatyfit', 'legday', 'fitnessgoals', 'fitnessgains', 'aesthetic', 'aesthetics', 'natural', 'powerlifting', 'fitnessking', 'fitnessphysique', 'weightlifting', 'fitnessbench', 'deadlift', 'fitnesssquats', 'workhard', 'goodnight', 'supernatural\n\n', '', '', '', '', '\n\n', '', '', '', '', '\n\n', '', '', '', 'fitnesssuperman', 'fitnessinstapic', 'instagramfitness', 'fitnessinspiration', 'hulk', 'beastmode', 'fitnessblessed', 'nyc', 'stillstanding', 'constantfitness', 'lifeisgood', 'pole', 'poledance', 'fitnesspoledancer', 'poledancenation', 'fitnessdance', 'fitnessdancer', 'polefit', 'polefitness', 'fitover40', 'fitmom', 'fitnesspolespin', 'poleshape', 'fitnesspolesport', 'polestrength', 'poleworkout', 'unitedbypole', 'fitnessart', 'fit', 'fitnessmotivation\n\n', '', '', '', '', '\n\n', '', '', '', '', '\n\n', '', '', '', 'fitnessmodel', 'fitfam', 'fitspo', 'motivationfitnow', 'fitnessmodel', 'instagood', 'instafit', 'gymlifestyle', 'gymtraining', 'fitnessgainz', 'gymrat', 'brolifestyle', 'fitlife', 'crossfit', 'fitnessstrength', 'fitnessmuscles', 'fitnessfaith', 'fitnessconsistency', 'noexcuseswork', 'fitnessfarmer', 'organicfit', 'fitgrow', 'healthfoods', 'fityouth', 'superfoods', 'dragonfruit', 'fitnesscom', 'fitbod', 'atlanticave', 'palmbeachfitness\n\n', '', '', '', '', '\n\n', '', '', '', '', '\n\n', '', '', '', 'fitnessnature', 'tropicalfruit', 'exoticfruit', 'fitnessfashion', 'fitnessgirl', 'fitnessmom', 'transformations', 'fitnesslife', 'abs', 'train', 'healthylifestyle', 'sisepuede', 'fitnesstattoo', 'tattoossometimes', 'fridaynight', 'gymsession', 'weightloss', 'legsgains', 'ladybeast', 'triplet', 'fitnessjourney', 'fitnesslifestyle', 'fitnessfreak', 'girlswholift', 'nopainnogain', 'getstrong', 'mondaymiles', 'chestday', 'seenonmyrun', 'trainhard']
        
        , amount=10)