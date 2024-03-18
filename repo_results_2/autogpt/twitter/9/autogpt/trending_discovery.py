

def recommend_users_to_follow(user, users, N):
    recommended_users = []
    for other_user in users:
        if other_user != user and len(user.following & other_user.following) > 0:
            recommended_users.append(other_user)
    recommended_users.sort(key=lambda user: len(user.following), reverse=True)
    return recommended_users[:N]