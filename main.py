import ClassManager

def main():
    user = ('John', '4045094520', 'EST')
    time_for_next_message = '17:30'
    new_message = (2, '608 Lauder Circle, Woodstock, GA', 'HOME', 34.08528518676758, -84.45832061767578, 'DAILY', 1,1,1,1,1,1,1, time_for_next_message)
    # ClassManager.class_manager.databasemanager.add_new_message_for_user_to_db(new_message)
    ClassManager.class_manager.databasemanager.lookup_time_and_date_to_determine_next_messages_to_send_out()


if __name__ == "__main__":
    main()



