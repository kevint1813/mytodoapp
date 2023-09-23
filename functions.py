def getlist():

    """
    will be called to access the txt file in main script.
    """

    with open("List.txt", "r") as local_file:
        local_list = local_file.readlines()
    return local_list


def writelist(local_list):

    """
    will be called to save the edits made in main script to the txt file.
    """

    with open("List.txt", "w") as local_file:
        local_file.writelines(local_list)
