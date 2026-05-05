#!/bin/bash
# -- Listing privileges for specific MySQL users --

# Define the users to check
USERS=("user_0d_1" "user_0d_2")

echo "--- Fetching Privileges for MySQL Users ---"

# Loop through the array and execute the SHOW GRANTS command
for USER in "${USERS[@]}"
do
    echo ""
    echo "Privileges for [$USER]:"
    # -u root: runs as root
    # -p: prompts for password
    # -e: executes the quoted SQL command
    mysql -u root -p -e "SHOW GRANTS FOR '$USER'@'localhost';" 2>/dev/null
    # Check if the previous command failed (e.g., user doesn't exist)
    if [ $? -ne 0 ]; then
        echo "Error: Could not retrieve grants for '$USER'. Ensure the user exists and your password is correct."
    fi
done

echo ""
echo "--- Task Complete ---"
