# Install Python and configure python
sudo apt install -y python3
sudo apt install -y python-pip
pip install tweepy
pip install pandas

# Run The Web Crawler file to generate info.csv
python src/crawler/Crawl.py

# Install Java
apt install openjdk-11-jre-headless

# Install Maven
apt install -y maven

# Maven Builds
mvn clean
mvn test
mvn install
mvn site

# Move Crawler output Excel file to Sentimental Analysis workspace
mv src/crawler/info.csv src/sentimental_analysis

# Install Machine Learning libraries
pip install keras
pip install tensorflow

# Move to Machine Learning folder from Crawler folder
cd ..
cd sentimental_analysis

# Switch case to select Machine Learning Model
echo "Sentimental Analysis Use cases"

# Option Menu
echo "1) Random Forest"
echo "2) Decision Tree"
echo "3) Naive Bayes"
read -p "Enter your choice: " ch

# Switch case
case "$ch" in
1) python randomforest.py ;;

2) python decisiontree.py ;;

3) python naivebayes.py ;;

esac

# Visualization
cd ..
cd visualization
python matplotlib.py


