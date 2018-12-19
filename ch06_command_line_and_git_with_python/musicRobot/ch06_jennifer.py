#Coursework: Fabiana & Jennifer - SuperRobotTask

class musicRobot(object):
    def __init__ (self, firstName, starSign):
        self.firstName = firstName
        self.starSign = starSign

    def musicType(self):
     #   starSign = musicRobot()
        if self.starSign == 'Capricorn':
            print('We think Jazz Music is the perfect sound for your zodiac! Some upbeat jazz that\'s full of energy! We think you would love Lady Gaga! She switches it up all the time!')
            
        elif self.starSign == 'Aquarius':
            print('Electronic Dance Music fits your zodiac! You love the build up to the chorus then you go absolutely nuts! David Guetta, Will.i.Am or Zedd might float your boat!')
            
        elif self.starSign == 'Pisces':
            print('Indie Pop fits your zodiac! You love those unusual sounds that have a story to their lyrics. Check out Lorde or The Cardigans! ou might just like them!')
            
        elif self.starSign == 'Aries':
            print("Rock fits your zodiac! Rocking until you are completely dizzy and have no idea where you are! The Rolling Stones, Aerosmith or Guns'n'Roses will definitely work for you! Check them out!")
            
        elif self.starSign == 'Taurus':
            print('Reggae fits your zodiac! Mellow sounds and a good beat. You have to check out the legendary Bob Marley and UB40!')
            
        elif self.starSign == 'Gemini':
            print('Dance Music fits your zodiac! Fun lyrics or lyrics that tell a story, as long as the sounds are catchy and get your heart pumping, you\'re in for a good time! Check out David Guetta or Avicii!') 
            
        elif self.starSign == 'Cancer':
            print('Blues fits your zodiac! Powerful riffs, trumpets, piano.. best sounds you can find. We think Eric Clapton and Stevie Wonder may be for you!')
            
        elif self.starSign == 'Leo':
            print('Heavy Metal fits your zodiac! Strong electronic guitars, heavy drums and even heavier voices with notes you probably can\'t reach! Try Iron Maiden, Black Sabbath or Metallica!')
            
        elif self.starSign == 'Virgo':
            print('Classical fits your zodiac! No words are needed. The music stirs your emotions. Listen to Ludovico Einaudi or Phillip Glass.')
            
        elif self.starSign == 'Libra':
            print("R'n'B fits your zodiac! You can always find a beat when you play any song from this genre! Aaliyah, Boyz II Men and Destiny\'s Child is soo you!")
            
        elif self.starSign == 'Scorpio':
            print('Afrobeats fits your zodiac! Whether you have heard of it or not, this will definitely add some seasoning to your entire existence! Check out Fally Ipupa, Davido and Wizkid!')
            
        elif self.starSign == 'Sagittarius':
            print('Hip Hop fits your zodiac! Hip Hop Horrraaayyyy, Hooooooooo!!!!! No description needed! Check out B.I.G. , 2Pac and Busta Rhymes. Thank me later!')
            
        else:
            print('You sure you typed that right? Type again!')
            