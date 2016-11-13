class Character:
    
    leftCounter = 0
    rightCounter = 0
    upCounter = 0
    downCounter = 0

    def __init__(self, hp, mp, deff, vit, wis, dex, att, spd):
        self.hp = hp;
        self.mp = mp;
        self.deff = deff;
        self.vit = vit;
        self.wis = wis;
        self.dex = dex;
        self.att = att;
        self.spd = spd;

    def shoot():
        pass

    def leftWalk():
        leftCounter += 1
        if leftCounter < 20
            characterSprite = pygame.image.load("WizardLeft1.png").convert_alpha()
        elif leftCouter < 39
            characterSprite = pygame.image.load("WizardLeft2.png").convert_alpha()
        else
            leftCounter = 0
            
    def rightWalk():
        rightCounter += 1
        if rightCounter < 20
            characterSprite = pygame.image.load("WizardRight1.png").convert_alpha()
        elif rightCounter < 39
            characterSprite = pygame.image.load("WizardRight2.png").convert_alpha()
        else
            rightCounter = 0
            
    def upWalk():
        upCounter += 1
        if upCounter < 20
            characterSprite = pygame.image.load("WizardUp1.png").convert_alpha()
        elif upCounter < 39
            characterSprite = pygame.image.load("WizardUp2.png").convert_alpha()
        else
            upCounter = 0
            
    def downWalk():
        downCounter += 1
        if downCounter < 20
            characterSprite = pygame.image.load("WizardDown1.png").convert_alpha()
        elif downCounter < 39
            characterSprite = pygame.image.load("WizardDown2.png").convert_alpha()
        else
            downCounter = 0
            
    def release():
        leftCounter = 0
        rightCounter = 0
        downCounter = 0
        upCounter = 0
        characterSprite = pygame.image.load("WizardUp1.png").convert_alpha()
