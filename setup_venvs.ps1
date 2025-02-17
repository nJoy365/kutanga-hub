# Define the list of microservices
$services = @("auth_service", "game_server_service", "monitoring_service")

# Navigate to the backend directory
cd backend

# Loop through each service
foreach ($service in $services) {
    Write-Host "Setting up virtual environment for $service..."

    # Navigate into the service directory
    cd $service

    # Create a virtual environment named 'venv'
    python -m venv venv

    # Activate the virtual environment
    .\venv\Scripts\Activate

    # Install required dependencies (modify as needed)
    if ($service -eq "auth_service") {
        pip install fastapi uvicorn pydantic sqlalchemy alembic bcrypt pyjwt
    }
    elseif ($service -eq "game_server_service") {
        pip install fastapi uvicorn sqlalchemy psutil
    }
    elseif ($service -eq "monitoring_service") {
        pip install fastapi uvicorn psutil redis
    }

    # Generate requirements.txt
    pip freeze | Out-File -Encoding utf8 requirements.txt

    # Deactivate the virtual environment
    deactivate

    # Move back to the backend directory
    cd ..
}

Write-Host "Virtual environments and requirements.txt files created successfully!"
