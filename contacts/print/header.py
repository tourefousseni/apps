from reportlab.platypus import Table, Image

def genHeaderTable(width, height):

    WidthList = [
        width * 55/100,
        width * 45/100,

    ]

    leftImgPath = '/Users/toure/PycharmProjects/douniyasoba/photos/identite/ZONE_DETUDE.jpg'
    leftImgWidth = WidthList[0]
    leftImg= Image(leftImgPath, leftImgWidth, height)

    rightImgPath = '/Users/toure/PycharmProjects/douniyasoba/photos/identite/Pantalon6.jpg'
    rightImgWidth = WidthList[0]
    rightImg = Image(rightImgPath, rightImgWidth, height)

    res = Table([
        [leftImg, rightImg]
    ],

    WidthList,
    height)

    res.setStyle([
         ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0,),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0,),
    ])

    return res