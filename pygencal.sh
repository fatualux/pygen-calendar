#!/bin/bash

# Read configuration from venv.cfg file
source ./pygencal.cfg

deactivate_venv() {
  echo "Deactivating virtual environment..."
  deactivate
  echo "Virtual environment deactivated."
}

# Trap Ctrl+C and call deactivate_venv function
trap deactivate_venv SIGINT

dependency_check() {
  if command -v virtualenv &> /dev/null; then
    echo "vOk, virtualenv package is installed on your system."
    export VENV_COMMAND=virtualenv
  else
    echo "A suitable Python virtual environment is not installed on your system."
    echo "Please install virtualenv and try again."
    echo "Aborting..."
    exit
  fi
}

venv_create() {
  echo "Starting Python Virtual Environment setup..."
  echo ""
  echo "Python Virtual Environment not found. Creating..."
  $VENV_COMMAND $WORKDIR
  echo ""
  echo "Python virtual environment created."
  echo ""
}

copy_files() {
  echo "Copying requirements..."
  cp $REQUIREMENTS_FILE $WORKDIR
  echo "Copying application file..."
  cp $APP_FILE $WORKDIR
  echo "Copying static files..."
  cp -r $STATIC_FILE $WORKDIR
  echo "Copying template files..."
  cp -r $TEMPLATE_FILE $WORKDIR
  echo "Copying modules..."
    cp -r $UTILS_FILE $WORKDIR
  echo ""
  echo "Done."
}

venv_activate() {
  echo "Activating virtual environment..."
  source $WORKDIR/bin/activate
  echo ""
}

install_req() {
  echo "Installing requirements..."
  pip install --upgrade pip && pip install -r $REQUIREMENTS_FILE
  echo ""
  echo "Done."
}

venv_verify() {
  if [ -d "$WORKDIR" ]; then
    venv_activate
    install_req
  else
    venv_create
    copy_files
    venv_activate
    install_req
  fi
}


starting_app() {
  echo "Starting application..."
  echo ""
  cd $WORKDIR && python $APP_FILE
}

dependency_check
venv_verify
starting_app