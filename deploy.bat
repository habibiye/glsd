echo "Adding to repository ."
git add .
echo "Commiting ..."
git commit -m "glsd"
echo "Pushing to heroku"
git push heroku master
echo "Deployment complete"
heroku open