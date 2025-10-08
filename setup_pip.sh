#!/bin/bash
#
# Setup pip to use private PyPI server for CoolAI packages
#
# Usage: ./setup_pip.sh <ip> <username> <password>
#

set -e

# Check arguments
if [ $# -ne 3 ]; then
    echo "Usage: $0 <ip> <username> <password>"
    echo ""
    echo "Example:"
    echo "  $0 192.168.1.100 admin mypassword"
    exit 1
fi

PYPI_IP=$1
PYPI_USERNAME=$2
PYPI_PASSWORD=$3

echo "=================================================="
echo "Configuring pip for private PyPI server"
echo "=================================================="

# Create pip config directory
PIP_CONFIG_DIR="$HOME/.pip"
PIP_CONFIG_FILE="$PIP_CONFIG_DIR/pip.conf"

mkdir -p "$PIP_CONFIG_DIR"

# Create pip.conf with private repository
cat > "$PIP_CONFIG_FILE" << EOF
[global]
index-url = http://${PYPI_USERNAME}:${PYPI_PASSWORD}@${PYPI_IP}:8080/simple/
trusted-host = ${PYPI_IP}

[install]
trusted-host = ${PYPI_IP}
EOF

echo ""
echo "✅ pip.conf created at: $PIP_CONFIG_FILE"
echo ""
echo "Configuration:"
echo "  Index URL: http://${PYPI_USERNAME}:***@${PYPI_IP}:8080/simple/"
echo "  Trusted Host: ${PYPI_IP}"
echo ""
echo "Test with:"
echo "  pip install coolai-data-models"
echo ""
echo "=================================================="

