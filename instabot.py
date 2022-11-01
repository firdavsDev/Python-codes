from instapy import InstaPy

ses=InstaPy(username = "it__pro",password="code",headless_browser=True)
ses.login()

ses.set_relationship_bounds(enabled=True, max_followers=200)
ses.set_do_follow(True,percentage=100)
ses.like_by_tags(["IT","followforfollow"],amount=3)
ses.set_dont_like(["nsfw"])

# ses.unfollow_users(amount=6,allFollowing=True,sleep_delay=60)

ses.end()

