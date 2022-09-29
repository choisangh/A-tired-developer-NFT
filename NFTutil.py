import random

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
def all_images_unique(all_images):
    seen=list()
    return not any(i in seen or seen.append(i) for i in all_images)