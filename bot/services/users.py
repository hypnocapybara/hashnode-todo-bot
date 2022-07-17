from bot.models import User


async def get_or_create_user(
        user_id: str,
        first_name: str,
        last_name: str,
        username: str,
) -> ('User', bool):
    created = False
    user = await User.query.where(User.telegram_user_id == user_id).gino.first()
    if not user:
        user = await User.create(
            telegram_user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        created = True

    return user, created
