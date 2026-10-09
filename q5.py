likes=[13,345,567,346,78]
def social_media(likes):
    mx_like=max(likes)
    sum_like=sum(likes)
    for i in likes:
        if i>=100:

          print(f"{i}")

    print(f"highest likes{mx_like}")
    print(f"total likes {sum_like}")
social_media(likes)