import ClassManager

def main():
    user = ('John', '4045094520', 'EST')
    new_message = (2, '608 Lauder Circle, Woodstock, GA', 'HOME', 34.08528518676758, -84.45832061767578, 'DAILY', 1,1,1,1,1,1,1, '17:15')
    ClassManager.class_manager.databasemanager.add_new_message_for_user_to_db(new_message)
    ClassManager.class_manager.databasemanager.add_user(user)

if __name__ == "__main__":
    main()



