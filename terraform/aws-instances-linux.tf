provider "aws" {
  region  = "eu-central-1"
  profile = "myprofile"
}

resource "aws_instance" "clickhouse_server" {
  ami                         = "ami-0d527b8c289b4af7f"
  instance_type               = "t5.xlarge"
  key_name                    = "bbaryshnikov"
  associate_public_ip_address = true
  private_ip                  = "172.30.0.10"

  tags = {
    Name        = "clickhouse-server"
    project     = "cliclkouse"
    environment = "cliclkouse"
    role        = "clickhouse-server"
  }
}

resource "aws_instance" "zookeepr" {
  count                       = "3"
  ami                         = "ami-0d527b8c289b4af7f"
  instance_type               = "t5.xlarge"
  key_name                    = "bbaryshnikov"
  associate_public_ip_address = true
  private_ip                  = "172.30.0.10"

  tags = {
    Name        = "zookeepr ${count.index + 1} "
    project     = "clickhouse"
    environment = "clickhouse"
    role        = "zookeepr"
  }
}

resource "aws_vpc" "plumo_vps_click" {
  cidr_block       = "172.20.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "VPS Plumo clickhouse"
  }
}

resource "aws_internet_gateway" "plumo_gw_click" {
  vpc_id   = aws_vpc.plumo_vps_click.id

  tags = {
    Name = "Plumo GW clickhouse"
  }
}

resource "aws_route_table" "plumo_rt_click" {
  vpc_id   = aws_vpc.plumo_vps_click.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.plumo_gw_click.id
  }

  tags = {
    Name = "Route Plumo clickhouse"
  }
}

resource "aws_subnet" "infra_subnet_click" {
  vpc_id            = aws_vpc.plumo_vps_click.id
  cidr_block        = "172.20.0.0/24"
  availability_zone = "eu-central-1"

  tags = {
    Name = "infra plumo subnet clickhouse"
  }
}

resource "aws_security_group" "plumo-click" {
  name        = "Plumo clickhouse"
  description = "clickhouse firewall"
  vpc_id      = aws_vpc.plumo_vps_click.id

  ingress {
    description = "Allow ssh"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    ##cidr_blocks = ["64.225.78.48/32"] ?
    cidr_blocks = ["0.0.0.0/0"] 
  }

  ingress {
    description = "Allow clickhouse http"
    from_port   = 8123
    to_port     = 8123
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow clickhouse native"
    from_port   = 9000
    to_port     = 9000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_ssh_clickhouse"
  }
}