#!bin/bash
echo "Installing k3d"
wget -q -O - https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash 

echo "+++++++++++++++++++++++++========================================++++++++++++++++++++++++++++++"
echo "Creating cluster with the name of <super-cluter> with one control plane and 3 worker node" 
k3d cluster create super-cluster --servers 1 --agents 3 --image rancher/k3s:latest