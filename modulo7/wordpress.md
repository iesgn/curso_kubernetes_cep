# Ejemplo completo: Despliegue y acceso a WordPress + MariaDB

kubectl create cm bd-datos --from-literal=bd_user=user_wordpress \
                           --from-literal=bd_dbname=wordpress
                           


kubectl create secret generic bd-passwords --from-literal=bd_password=password1234 \
                                           --from-literal=bd_rootpassword=root1234


