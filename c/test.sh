export SR_POST_CONFIG="`pwd`/post.conf"
export LD_PRELOAD=`pwd`/libsrshim.so.1.0.0

cp libsrshim.c ~/test/hoho_my_darling.txt
ln -s hoho haha
rm haha
