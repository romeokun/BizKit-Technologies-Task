from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    
    if(len(args) <= 0):
        return USERS
    
    PARAMS = ["id", "name", "age", "occupation"]
    result = [[] for x in range(4)]

    for user in USERS:
        print(user)
        for i in range(len(PARAMS)):
            if (PARAMS[i]) not in args:
                continue
            if i == 0 and (user.get(PARAMS[i]) == args.get(PARAMS[i])):
                result[i].append(user)
                break

            if (i == 1 or i == 3) and args.get(PARAMS[i]).lower() in user.get(PARAMS[i]).lower():
                result[i].append(user)
                break
            
            if i == 2 and int(args.get(PARAMS[i])) >= int(user.get(PARAMS[i]))-1 and int(args.get(PARAMS[i])) <= int(user.get(PARAMS[i]))+1: 
                result[i].append(user)
                break

    return [x for items in result for x in items]
