#
# Base Docker image for Wishlist
#
#
# This dockerfile simply installs all dependencies required by other wishlist images
#
# docker build --tag josephmuli/wishlist_base .
#

FROM ubuntu:15.10

MAINTAINER Joseph Muli <joseph.muli@andela.com>

# Install dependencies
RUN apt-get update;\
    apt-get install -y nodejs nodejs-legacy npm git \
        python-virtualenv python3-dev \
        libjpeg8-dev zlib1g-dev libwebp-dev \
        sudo
