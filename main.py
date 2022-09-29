from PIL import Image
from IPython.display import display
import random
import json
import os

skin=['white','yellow','black']
skin_weight=[30,40,30]

skin_files={
    "white": "white",
    "yellow": "yellow",
    "black": "black"

}

eyebrow=['high','mid','low']
eyebrow_weight=[30,40,30]

eyebrow_files = {
    "high": "high",
    "mid": "mid",
    "low": "low"

}


hair=['hair1']
hair_weight=[100]

hair_files = {
    "hair1": "hair1"

}


desk=['desk1']
desk_weight=[100]

desk_files = {
    "desk1": "desk1"

}



jean=['jean1']
jean_weight=[100]

jean_files = {
    "jean1": "jean1"

}


computer=['computer1']
computer_weight=[100]

computer_files = {
    "computer1": "computer1"

}






cloth=['cloth1']
cloth_weight=[100]

cloth_files = {
    "cloth1": "cloth1"

}

chair=['chair1']
chair_weight=[100]

chair_files = {
    "chair1": "chair1"

}

bg=['bg1','bg2','bg3','bg4','bg5','bg6']
bg_weight=[15,15,15,20,15,20]

bg_files = {
    "bg1": "bg1",
    "bg2": "bg2",
    "bg3": "bg3",
    "bg4": "bg4",
    "bg5": "bg5",
    "bg6": "bg6"

}




TOTAL_IMAGES = 30

all_images=[]

def create_new_image():
    new_image={}

    new_image['skin']=random.choices(skin,skin_weight)
    new_image['eyebrow'] = random.choices(eyebrow, eyebrow_weight)
    new_image['hair'] = random.choices(hair, hair_weight)
    new_image['desk'] = random.choices(desk, desk_weight)
    new_image['jean'] = random.choices(jean, jean_weight)
    new_image['computer'] = random.choices(computer, computer_weight)
    new_image['cloth'] = random.choices(cloth, cloth_weight)
    new_image['chair'] = random.choices(chair, chair_weight)
    new_image['bg'] = random.choices(bg, bg_weight)

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image

for i in range(TOTAL_IMAGES):
    new_trait_image=create_new_image()
    all_images.append(new_trait_image)


# 고유성 검증

def all_images_unique(all_images):
    seen=list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?",all_images_unique(all_images))

i=0

for item in all_images:
    item["tokenId"]=i
    i=i+1

print(all_images)
for item in all_images:
    im1 = Image.open(f'./img/background/{bg_files[item["bg"][0]]}.png').convert('RGBA')
    im2 = Image.open(f'./img/skin/{skin_files[item["skin"][0]]}.png').convert('RGBA')
    im3 = Image.open(f'./img/chair/{chair_files[item["chair"][0]]}.png').convert('RGBA')
    im4 = Image.open(f'./img/clothes/{cloth_files[item["cloth"][0]]}.png').convert('RGBA')
    im5 = Image.open(f'./img/computer/{computer_files[item["computer"][0]]}.png').convert('RGBA')
    im6 = Image.open(f'./img/jean/{jean_files[item["jean"][0]]}.png').convert('RGBA')
    im7 = Image.open(f'./img/eyebrow/{eyebrow_files[item["eyebrow"][0]]}.png').convert('RGBA')
    im8 = Image.open(f'./img/hair/{hair_files[item["hair"][0]]}.png').convert('RGBA')
    im9 = Image.open(f'./img/desk/{desk_files[item["desk"][0]]}.png').convert('RGBA')

    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)
    com7 = Image.alpha_composite(com6, im8)
    com8 = Image.alpha_composite(com7, im9)



    rgb_im=com8.convert('RGB')
    file_name=str(item["tokenId"])+".png"
    rgb_im.save("./img/NFT/"+file_name)


