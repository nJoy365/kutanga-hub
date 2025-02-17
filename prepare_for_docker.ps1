# Define the list of microservices
$services = @("auth_service", "game_server_service", "monitoring_service")

# Navigate to the backend directory
cd backend

# Loop through each service
foreach ($service in $services) {
    Write-Host "Generating requirements.txt for $service..."

    # Navigate into the service directory
    cd $service

    # Check if venv exists before proceeding
    if (Test-Path "venv") {
        # Activate the virtual environment
        .\venv\Scripts\Activate

        # Generate requirements.txt
        pip freeze | Out-File -Encoding utf8 requirements.txt

        # Deactivate virtual environment
        deactivate

        Write-Host "requirements.txt created for $service"
    }
    else {
        Write-Host "No virtual environment found for $service. Skipping..."
    }

    # Remove the virtual environment folder
    if (Test-Path "venv") {
        Remove-Item -Recurse -Force "venv"
        Write-Host "Removed virtual environment for $service"
    }

    # Move back to the backend directory
    cd ..
}

Write-Host "All requirements.txt files generated and virtual environments removed! Ready for Docker setup. 🚀"
