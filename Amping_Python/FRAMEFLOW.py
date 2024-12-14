#Password: FrameFlowPython
from datetime import datetime  # Import datetime module to handle date

#=======================================================================================================
#=========================================================== Function for Photography Services
#=======================================================================================================

def PhotographyServices():
    print("Details: ")
    price = 4000.00  # Initial price for photography service

    # Photo Album selection
    detail1 = input("\t\t Photo Album - Php 3,000.00 (Y/N): ")
    if detail1 == 'Y' or detail1 == 'y':
        detail1 = 'Included. Php 3,000.00'
        price += 3000.00  # Add 3000 if photo album is selected
    elif detail1 == 'N' or detail1 == 'n':
        detail1 = 'None'  # No photo album if the user selects N/n
    else:
        print("**** Invalid input. Please enter 'Y' or 'N'. ****")
        return PhotographyServices()  

    # Framed Photos selection
    detail2 = input("\t\t Framed Photos - Php 1,000.00 per frame (Y/N): ")
    if detail2 == 'Y' or detail2 == 'y':
        detail2 = 'Included. Php 1,000.00'
        while True:
            try:
                frameNum = int(input("\t\t Number of Frames: "))  
                if frameNum < 0:
                    print("**** Please enter a positive number for the number of frames. *****")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for frames.")
        price += 1000.00 * frameNum  # Add price based on the number of frames
    elif detail2 == 'N' or detail2 == 'n':
        detail2 = 'None'  # No framed photos if the user selects N/n
    else:
        print("**** Invalid input. Please enter 'Y' or 'N'. ****")
        return PhotographyServices()  

    return [detail1, detail2], price  # Return details as a list and the calculated price


#=======================================================================================================
#=========================================================== Function for Videography Services
#=======================================================================================================

def VideographyServices():
    print("Details: ")
    price = 9000  # Initial price for videography service
    print("\t\t V11 - Standard Videography (Captures highlights in the event. Includes 1 videographer.) - Php 9,000 \n\t\t V12 - Creative Videography (Captures main event with a cinematic touch. Includes 2 videographers) - Additional Php 4,000.00")

    detail3 = input("\t\t Enter type of videography (V11/V12): ")
    if detail3 == 'V12' or detail3 == 'v12':
        detail3 = 'Creative Videography. Php 4,000.00'
        price += 4000.00  # Add 4000 for the second videographer 
    elif detail3 == 'V11' or detail3 == 'v11':
        detail3 = 'Standard Videography. '
    else:
        print("**** Invalid input for videography type. Please choose 'V11' or 'V12'.****")
        return VideographyServices() 

    detail4 = input("\t\t Same Day Edit - Php 1,000.00 (Y/N): ")
    if detail4 == 'Y' or detail4 == 'y':
        detail4 = 'Included. Php 1,000.00'
        price += 1000.00  # Add 1000 for Same Day Edit
    elif detail4 == 'N' or detail4 == 'n':
        detail4 = 'None'  # If the user choonses no Same Day Edit
    else:
        print("**** Invalid input. Please enter 'Y' or 'N'. ****")
        return VideographyServices() 

    detail5 = input("\t\t Aerial - Php 1,500.00 (Y/N): ")
    if detail5 == 'Y' or detail5 == 'y':
        detail5 = 'Included. Php 1,500.00'
        price += 1500.00  # Add 1500 for Aerial service
    elif detail5 == 'N' or detail5 == 'n':
        detail5 = 'None'  # If the user chooses no Aerial service
    else:
        print("**** Invalid input. Please enter 'Y' or 'N'. ****")
        return VideographyServices() 

    return [detail3, detail4, detail5], price  # Return videography details as a list and the calculated price


#=======================================================================================================
#================================================= Function for checking existing appointments
#=======================================================================================================

def checkExistingAppointments(eventDate, eventTime):
    try:
        with open("appointments.txt", "r") as file:
            appointments = file.readlines()
            
            # Initialize a count for the number of appointments for the same date and time
            appointment_count = 0
 
            # This would check if the same client booked the same date and time. This would ensure that there would be no double Bookings
            for line in appointments:
                if f"Event Date: {eventDate}" in line and f"Event Time: {eventTime}" in line:
                    appointment_count += 1

                # If there are already 7 appointments for the same date and time, return True
                if appointment_count >= 7:
                    return True
    
            return False
        
    except FileNotFoundError:
        return False  # If the file doesn't exist, it's okay to proceed


#=======================================================================================================
#=============================================================== Function for booking an event
#=======================================================================================================

def scheduleAppointment():
    # Create a unique Appointment ID
    appointmentID = f"APP{int(datetime.now().timestamp())}"  # Generate a unique ID based on timestamp

    print("         \nEnter Client Information: ")
    clientName = input("\t\t Client Name: ")
    clientContact = input("\t\t Client Contact Number: ")
    clientEmail = input("\t\t Client Email Address: ")
    eventType = input("\t\t Type of Event (Wedding / Birthday / Christening): ")
    eventAddress = input("\t\t Address of the event: ")

    # Handle event date
    while True:  # Enter a while loop with error handling for event date
        eventDate_str = input("\t\t Date of event (format YYYY-MM-DD): ")
        try:
            # Convert string to date
            eventDate = datetime.strptime(eventDate_str, '%Y-%m-%d').date()

            # Check if the event date is in the past
            if eventDate <= datetime.now().date():
                print("**** Selected date cannot be scheduled in the past. ****")
            else:
                break  # Exit the loop if the date is valid

        except ValueError:
            print("**** Invalid date format. Please use the correct format: YYYY-MM-DD. ****")

    # Handle event time
    while True:  # Enter a while loop with error handling for event time
        eventTime_str = input("\t\t Time of the event (Use a 24-hour format | HH:MM): ")
        try:
            eventTime = datetime.strptime(eventTime_str, '%H:%M').time()  # Convert string to time
            break  
        except ValueError:
            print("**** Invalid time format. Please use HH:MM. ****")

    # Check if the entered date and time already have 3 appointments
    if checkExistingAppointments(eventDate, eventTime):  # Pass eventDate and eventTime here
        print("**** The date and time are already fully booked. Please choose another date or time. ****")
        return None  # Exit if the date and time are fully booked

    while True:
        print("Services:\n\t\t P1 - Photography Services (Php 4,000.00) \n\t\t V1 - Videography Services (Php 9,000.00)")
        service = input("\t\t Select Service: ")

        # Initialize photo_details and video_details to None
        photo_details = None
        video_details = None
        price = 0

        # Capture details based on selected service
        if service == 'P1' or service == 'p1':
            photo_details, price = PhotographyServices()
            break  # Exit the loop after valid input for photography
        elif service == 'V1' or service == 'v1':
            video_details, price = VideographyServices()
            break  # Exit the loop after valid input for videography
        else:
            print("**** Invalid Service selection. Enter only P1 or V1. ****")


    confirmation = input("\t\t Confirm details (Y/N): ")

    if confirmation == 'Y' or confirmation == 'y':

        # Capture current date when appointment is confirmed
        confirmationDate = datetime.now().date()

        # Save appointment data to a text file Named appointment.txt
        with open("appointments.txt", "a") as file:  # Open the file in append mode
            file.write(f"Appointment ID: {appointmentID}\n")  # Save Appointment ID
            file.write(f"Client Name: {clientName}\n")
            file.write(f"Client Contact Number: {clientContact}\n")
            file.write(f"Client Email Address: {clientEmail}\n")
            file.write(f"Type of Event: {eventType}\n")
            file.write(f"Event Address: {eventAddress}\n")
            file.write(f"Event Date: {eventDate}\n")
            file.write(f"Event Time: {eventTime}\n")
            file.write(f"Selected Service: {service}\n")

            # Handle both photography and videography details separately
            if service == 'P1' or service == 'p1':
                if photo_details:
                    file.write(f"Photography Service Details: \n + + Photography Service Price - Php 6,000.00 \n + + Photo Album - {photo_details[0]}, \n + + Framed Photos - {photo_details[1]}\n")
            elif service == 'V1' or service == 'v1':
                if video_details:
                    file.write(f"Videography Service Details: \n + + Videography Service Price - Php 9,000.00 \n + + {video_details[0]} \n + + Same Day Edit - {video_details[1]} \n + + Aerial - {video_details[2]}\n")
 
            file.write(f"Total Price: Php. {price}\n")
            file.write(f"Appointment Confirmation Date: {confirmationDate}\n")  # Save the confirmation date
            file.write("="*50 + "\n")  # Add separator for readability
            
        
        # Save available appointments to a new file (used for easy readings in delete function)
        with open("avail_appointments.txt", "a") as file:  # Open the file in append mode so that previous records won't be replaced
            file.write(f"Appointment ID: {appointmentID} || ")  
            file.write(f"Client Name: {clientName} ||")
            file.write(f"Client Contact Number: {clientContact} || ")
            file.write(f"Event Date: {eventDate} || ")
            file.write(f"Appointment Scheduled: {confirmationDate}\n")
            file.write("="*50 + "\n")  # Add separator for readability


        # Call the printAppointment function to display the appointment details
        printAppointment(appointmentID, clientName, clientContact, clientEmail, service, photo_details, video_details, eventType, eventAddress, eventDate, eventTime, price, confirmationDate)
        print("\n\t\tAppointment details saved successfully!")

            # Calculate the number of days until the event
        current_date = datetime.now().date()  # Get today's date
        days_until_event = (eventDate - current_date).days 

        # Print message indicating how many days from now the event is
        print(f"\n\t\tNote: Event Scheduled in {days_until_event} days from now.")

        return appointmentID, clientName, clientContact, clientEmail, service, photo_details, video_details, eventType, eventAddress, eventDate, eventTime, price
    
    elif confirmation == 'N' or confirmation == 'n':
        return None  # Exit if the user cancels
    else:
        print("**** Invalid Input. Please try again. ****")
        return scheduleAppointment()  # Retry if input is invalid

#=======================================================================================================
#================================================ Function for displaying scheduledAppointment
#=======================================================================================================

def printAppointment(appointmentID, clientName, clientContact, clientEmail, service, photo_details, video_details, eventType, eventAddress, eventDate, eventTime, price, confirmationDate):
    print("\n\n= + = + = + = + = + = + =     APPOINTMENT DETAILS     = + = + = + = + = + = + =\n")
    print(f"Appointment ID: {appointmentID}\n")
    print(f"\t\t Client Name: {clientName}")
    print(f"\t\t Client Contact Number: {clientContact}")
    print(f"\t\t Client Email Address: {clientEmail}")
    print(f"\t\t Type of Event (Wedding / Birthday / Christening): {eventType}")
    print(f"\t\t Address of the event: {eventAddress}")
    print(f"\t\t Date of event: {eventDate}")  # Display eventDate in date format
    print(f"\t\t Time of event: {eventTime}")  # Display eventTime in time format
    print(f"\t\t Selected Service: {service}")

    # Handle both photography and videography details separately
    if service == 'P1' or service == 'p1':
        if photo_details:
            print(f"\t\t Photography Service Details: \n\t\t + + Photography Service Price - Php 6,000.00 \n\t\t + + Photo Album - {photo_details[0]} \n\t\t + + Framed Photos - {photo_details[1]}\n")
    elif service == 'V1' or service == 'v1':
        if video_details:
            print(f"\t\t Videography Service Details: \n\t\t + + Videography Service Price - Php 9,000.00 \n\t\t + + {video_details[0]} \n\t\t + + Same Day Edit - {video_details[1]} \n\t\t + + Aerial - {video_details[2]}\n")

    print(f"\t\t Total Price: Php. {price}")  # Display the total price
    print(f"\t\t Appointment Confirmation Date: {confirmationDate}")  # Display the date when the appointment was confirmed
    print("\n= + = + = + = + = + = + = + = + = + = + = + = + = + = + = + = + = + = + = + = +\n")


#=======================================================================================================
#================================================= Function for DELETING appointment by ID
#=======================================================================================================

def deleteAppointment():

    viewAvailAppointments()

    appointmentID = input("\nEnter Appointment ID to delete: ")

    # Deletes that appointment entered from appointment.txt
    try:
        with open("appointments.txt", "r") as file:
            appointments = file.readlines()

        # Find the appointment block associated with the ID
        appointment_found = False
        new_appointments = []
        temp_block = []
        for line in appointments:
            if f"Appointment ID: {appointmentID}" in line:
                appointment_found = True
                temp_block.append(line) 
                continue  

            if appointment_found:
                temp_block.append(line)
                if line.strip() == "=" * 50:  # End of this appointment block
                    appointment_found = False  # Stop collecting this block
                    continue  # Skip adding this line to the new appointments list

            if not appointment_found:
                new_appointments.append(line)  # Collect all other lines not part of the block

        if appointment_found:
            print(f"\nAppointment with ID {appointmentID} has been fully removed.\n")
            return

        # Rewrite the updated list back into the file
        with open("appointments.txt", "w") as file:
            file.writelines(new_appointments)
        
        print(f"\nAppointment with ID {appointmentID} has been successfully deleted.\n")

    except FileNotFoundError:
        print("**** Appointments file not found. ****")


    # Deletes that appointment entered from avail_appointments.txt
    try:
        with open("avail_appointments.txt", "r") as file:
            appointments = file.readlines()

        # Find the appointment block associated with the ID
        appointment_found = False
        new_appointments = []
        temp_block = []
        for line in appointments:
            if f"Appointment ID: {appointmentID}" in line:
                appointment_found = True
                temp_block.append(line)  # Start collecting the block
                continue  # Skip adding this line, as it's part of the block

            if appointment_found:
                temp_block.append(line)
                if line.strip() == "=" * 50:  # End of this appointment block
                    appointment_found = False 
                    continue 

            if not appointment_found:
                new_appointments.append(line)  # Collect all other lines not part of the block

        if appointment_found:
            print(f"\nAppointment with ID {appointmentID} was not found or has been fully removed.\n")
            return

        # Rewrite the updated list back into the file
        with open("avail_appointments.txt", "w") as file:
            file.writelines(new_appointments)
        
        print(f"\nAppointment with ID {appointmentID} has been successfully deleted.\n")

    except FileNotFoundError:
        print("**** Appointments file not found. ****")


#=======================================================================================================
#================================================= Function for VIEWING all appointments
#=======================================================================================================

def viewAppointments():
    try:
        with open("appointments.txt", "r") as file:
            appointments = file.readlines()
            
            if len(appointments) == 0:
                print("**** No appointments found. ****")
                return

            # Display appointments in readable format
            print("\n+ + + ALL APPOINTMENTS AND DETAILS: + + +\n")
            appointment_block = []
            for line in appointments:
                appointment_block.append(line.strip())  # Add each line to the current block

                # If a separator line (====) is found, print the current appointment and start a new block
                if line.strip() == "=" * 50:
                    print("\n".join(appointment_block))  # Print the full appointment block
                    print("=" * 50)  # Print separator between appointments
                    appointment_block = []  # Reset for the next appointment

            # Handle case where file doesn't have the separator at the end
            if appointment_block:
                print("\n".join(appointment_block))  # Print last block if exists
                print("=" * 50)  # Final separator for the last appointment

    except FileNotFoundError:
        print("**** Appointments file not found. ****")

#=======================================================================================================
#================================================= Function for VIEWING avail_appointments()
#=======================================================================================================

def viewAvailAppointments():
    try:
        with open("avail_appointments.txt", "r") as file:
            appointments = file.readlines()
            
            if len(appointments) == 0:
                print("\nNo appointments found.")
                return

            # Display appointments in readable format
            print("\n + + + SCHEDULED APPOINTMENTS: + + +\n")
            appointment_block = []
            for line in appointments:
                appointment_block.append(line.strip())  # Add each line to the current block

                # If a separator line (====) is found, print the current appointment and start a new block
                if line.strip() == "=" * 50:
                    print("\n".join(appointment_block))  # Print the full appointment block
                    print("=" * 50)  # Print separator between appointments
                    appointment_block = []  # Reset for the next appointment

            # Handle case where file doesn't have the separator at the end
            if appointment_block:
                print("\n".join(appointment_block))  # Print last block if exists
                print("=" * 50)  # Final separator for the last appointment

    except FileNotFoundError:
        print("**** Appointments file not found. ****")

#=======================================================================================================
#================================================= MAIN MENU INTERFACE function for user options
#=======================================================================================================

def Option():
    while True:
        print("======================================================================")
        print("                            FrameFlow")
        print("     Photography and Videography Services Appointment System")
        print("======================================================================")
        print("        Select from the following options: \n\t\t\t A1 - Schedule an Appointment \n\t\t\t A2 - View Appointments \n\t\t\t A3 - Delete Appointment \n\t\t\t A4 - Description about the System \n\t\t\t A5 - Exit")
        
        optionChoice = input("\n\t\t Enter your choice: ")

        if optionChoice == 'A1' or optionChoice == 'a1':
            print("======================================================================")
            print("======================================================================") 
            print(f"\nChosen Option: {optionChoice}")
            scheduleAppointment() #Schedile Appointmesnt
        elif optionChoice == 'A2' or optionChoice == 'a2':
            print("======================================================================")
            print("======================================================================") 
            print(f"\nChosen Option: {optionChoice}")
            viewAppointments()  # View appiontments
        elif optionChoice == 'A3' or optionChoice == 'a3':
            print("======================================================================")
            print("======================================================================") 
            print(f"\nChosen Option: {optionChoice}")
            deleteAppointment()  # Delete appointment
        elif optionChoice == 'A4' or optionChoice == 'a4':
            print("======================================================================")
            print("======================================================================") 
            print(f"\nChosen Option: {optionChoice}")
            print("This system allows users to book and manage appointments for photography and videography services.")
        elif optionChoice == 'A5' or optionChoice == 'a5':
            print("======================================================================")
            print("======================================================================") 
            print(f"\nChosen Option: {optionChoice}")
            print("Exiting the System.") #By exit, this would go back to the adminPassword() function
            AdminPassword()
        else:
            print("**** Invalid Option. Select the appropriate code for the desired option.**** \n\n")


#=======================================================================================================
#========================================================================== PASSWORD for Admin
#=======================================================================================================

def AdminPassword():
    print("\n=========+==+===F=R=A=M=E=F=L=O=W======S=Y=S=T=E=M===+==+=========")     
    password = input ("\nEnter Password: ") #the password is: FrameFlowPython

    if password != 'FrameFlowPython':
        print("**** Your Password is Incorrect. Please Try again. ****")
        return AdminPassword()
    else:
        print("\n\t    Access Granted.")
        print("\t    Welcome to the FrameFlow System, Admin!\n")
    

#=======================================================================================================
#=========================================================================== CALLING Functions
#=======================================================================================================

AdminPassword() # calls the password option for the admin

Option() #calls the option function to display options a1, a2, a3, a4