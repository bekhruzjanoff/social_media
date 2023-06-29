from database.models import HashTag, Post, PostPhoto, PostComment, db


# Получить все посты
def get_all_posts_db():
    posts = Post.query.all()
    return posts


# Получить все изображения
def get_all_photo_db():
    photos = PostPhoto.query.all()
    return photos


# Получить определенный пост
def get_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    return post


# Удалить пост
def delete_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        db.session.delete(post)
        db.session.commit()


# Иззменить текст поста
def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        post.post_text = new_text
        db.session.commit()


# Добавить комментарий к посту
def add_comment_post_db(post_id, comment_user_id, comment_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        new_comment = PostComment(post_id=post_id, user_id=comment_user_id, comment_text=comment_text)
        db.session.add(new_comment)
        db.session.commit()


# Получить все комментарии для определенного поста
def get_comments_for_post(post_id):
    comments = PostComment.query.filter_by(post_id=post_id).all()
    return [comment.serialize() for comment in comments]


# Изменить текст комментария
def change_comment_text_db(comment_id, new_text, comment_user_id):
    comment = PostComment.query.get(comment_id, comment_user_id)
    if comment:
        comment.comment_text = new_text
        db.session.commit()


def delete_comment_db(comment_id, comment_user_id):
    comment = PostComment.query.get(comment_id, comment_user_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()


def get_all_hashtag_db(size):
    get_hashtag = HashTag.query.all()

    return get_hashtag[:size]


def get_exact_hashtag_db(hashtag_name):
    get_exact_hashtag = HashTag.filter_by(hashtag_name=hashtag_name).first()

    return get_exact_hashtag


#Получить определенную фоторгафию по photo_id
def get_exact_photo_db(photo_id):
    exact_photo = PostPhoto.query.filter_by(photo_id=photo_id).first()
    return exact_photo


#Получить все изображения определенного пользователя
def get_exact_user_photos_db(user_id):
    exact_user_photo = PostPhoto.query.filter_by(user_id=user_id).first()
    return exact_user_photo



#Изменить определенную фоторгафию пользователя по user_id и photo_id
def change_exact_user_photo_db(user_id, photo_id, photo_path):
    change_exact_user_photo = PostPhoto.query.filter_by(photo_id=photo_id, user_id=user_id).first()
    if change_exact_user_photo:
        change_exact_user_photo.photo_path = photo_path
        db.session.commit()


#Удаляем определенную фоторгафию пользователя по user_id и photo_id
def delete_exact_user_photo_db(user_id, photo_id, photo_path):
    delete_exact_user_photo = PostPhoto.query.filter_by(photo_id=photo_id, user_id=user_id).first()
    if delete_exact_user_photo:
        db.session.delete(delete_exact_user_photo)
        db.session.commit()
        return True
    return False


#Добавить новый пост
def add_new_post_db(user_id, photo_id, post_text):
    new_post = Post(user_id=user_id, photo_id=photo_id, post_text=post_text)
    db.session.add(new_post)
    db.session.commit()
    return True


from database.models import HashTag, Post, PostPhoto, PostComment, db


# Получить все посты
def get_all_posts_db():
    posts = Post.query.all()
    return posts


# Получить все изображения
def get_all_photo_db():
    photos = PostPhoto.query.all()
    return photos


# Получить определенный пост
def get_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    return post


# Удалить пост
def delete_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        db.session.delete(post)
        db.session.commit()


# Иззменить текст поста
def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        post.post_text = new_text
        db.session.commit()


# Добавить комментарий к посту
def add_comment_post_db(post_id, comment_user_id, comment_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        new_comment = PostComment(post_id=post_id, user_id=comment_user_id, comment_text=comment_text)
        db.session.add(new_comment)
        db.session.commit()


# Получить все комментарии для определенного поста
def get_comments_for_post(post_id):
    comments = PostComment.query.filter_by(post_id=post_id).all()
    return [comment.serialize() for comment in comments]


# Изменить текст комментария
def change_comment_text_db(comment_id, new_text, comment_user_id):
    comment = PostComment.query.get(comment_id, comment_user_id)
    if comment:
        comment.comment_text = new_text
        db.session.commit()


def delete_comment_db(comment_id, comment_user_id):
    comment = PostComment.query.get(comment_id, comment_user_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()


def get_all_hashtag_db(size):
    get_hashtags_incount = HashTag.query.all()
    if len(get_hashtags_incount) >= size:
        return get_hashtags_incount[:size]
    return False


def get_exact_hashtag_db(hashtag_name):
    get_exact_hashtag = HashTag.filter_by(hashtag_name=hashtag_name).all()
    if get_exact_hashtag:
        return get_exact_hashtag
    return False

# Добавить пост под хэштег
def create_post_for_hashtag(post_id, hashtags):
    created_hashtags = []

    for hashtag_name in hashtags:
        new_hashtag_post = HashTag(post_id=post_id, hashtag_name=hashtag_name)
        created_hashtags.append(new_hashtag_post)

    db.session.add_all(created_hashtags)
    db.session.commit()
    return True

#Получить определенную фоторгафию по photo_id
def get_exact_photo_db(photo_id):
    exact_photo = PostPhoto.query.filter_by(photo_id=photo_id).first()
    return exact_photo


#Получить все изображения определенного пользователя
def get_exact_user_photos_db(user_id):
    exact_user_photo = PostPhoto.query.filter_by(user_id=user_id).first()
    return exact_user_photo



#Изменить определенную фоторгафию пользователя по user_id и photo_id
def change_exact_user_photo_db(user_id, photo_id, photo_path):
    change_exact_user_photo = PostPhoto.query.filter_by(photo_id=photo_id, user_id=user_id).first()
    if change_exact_user_photo:
        change_exact_user_photo.photo_path = photo_path
        db.session.commit()


#Удаляем определенную фоторгафию пользователя по user_id и photo_id
def delete_exact_user_photo_db(user_id, photo_id, photo_path):
    delete_exact_user_photo = PostPhoto.query.filter_by(photo_id=photo_id, user_id=user_id).first()
    if delete_exact_user_photo:
        db.session.delete(delete_exact_user_photo)
        db.session.commit()
        return True
    return False


#Добавить новый пост
def add_new_post_db(user_id, photo_id, post_text):
    new_post = Post(user_id=user_id, photo_id=photo_id, post_text=post_text)
    db.session.add(new_post)
    db.session.commit()
    return new_post.post_id


# Загрузка фотографии
def post_new_photo_db(user_id, photo_path):
    new_post_photo = PostPhoto(user_id=user_id, photo_path=photo_path)
    db.session.add(new_post_photo)
    db.session.commit()


    return new_post_photo.photo_id