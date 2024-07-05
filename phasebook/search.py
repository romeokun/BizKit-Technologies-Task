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
        for i in range(len(PARAMS)):
            if PARAMS[i] not in args:
                continue

            toAppend = False
            match i:
                case 0:
                    toAppend = user.get(PARAMS[i]) == args.get(PARAMS[i])
                case 1:
                    toAppend = args.get(PARAMS[i]).lower() in user.get(PARAMS[i]).lower()
                case 2:
                    toAppend = int(args.get(PARAMS[i])) >= int(user.get(PARAMS[i]))-1 and int(args.get(PARAMS[i])) <= int(user.get(PARAMS[i]))+1
                case 3:
                    toAppend = args.get(PARAMS[i]).lower() in user.get(PARAMS[i]).lower()

            if toAppend:
                result[i].append(user)
                break


    return [x for items in result for x in items]
