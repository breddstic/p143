from flask import Flask, jsonify, request
import pandas as pd
from content_filtering import get_recommendations
from demographic_filtering import output
app = Flask(__name__)
articles_data = pd.read_csv("articles.csv")
liked_articles = []
not_liked_articles = []
all_articles = articles_data[['url', 'title', 'text', 'lang', 'total_events']]
@app.route("/get-article")
def get_article():
    article_data = {
        "title": all_articles[0][19],
        "poster_link": all_articles[0][27],
        "release_date": all_articles[0][13] or "N/A",
        "duration": all_articles[0][15],
        "rating": all_articles[0][20],
        "overview": all_articles[0][9]
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            "title": article[0],
            "poster_link": article[1],
            "release_date": article[2] or "N/A",
            "duration": article[3],
            "rating": article[4],
            "overview": article[5]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "poster_link": recommended[1],
            "release_date": recommended[2] or "N/A",
            "duration": recommended[3],
            "rating": recommended[4],
            "overview": recommended[5]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()

  render() {
    const { movieDetails } = this.state;
    if (movieDetails.poster_link) {
      const {
        poster_link,
        title,
        release_date,
        duration,
        overview,
        rating
      } = articles_data;

      return (
        <View style={styles.container}>
          <View style={styles.headerContainer}>
            <Header
              centerComponent={{
                text: "Article Recommended",
                style: styles.headerTitle
              }}
              rightComponent={{ icon: "search", color: "#fff" }}
              backgroundColor={"#d500f9"}
              containerStyle={{ flex: 1 }}
            />
          </View>
          <View style={styles.subContainer}>
            <View style={styles.subTopContainer}>
              <Image style={styles.posterImage} source={{ uri: poster_link }} />
            </View>
            <View style={styles.subBottomContainer}>
              <View style={styles.upperBottomContainer}>
                <Text style={styles.title}>{title}</Text>
                <Text style={styles.subtitle}>{`${
                  release_date.split("-")[0]
                } | ${duration}`}</Text>
              </View>
              <View style={styles.middleBottomContainer}>
                <View style={{ flex: 0.3 }}>
                  <AirbnbRating
                    count={10}
                    reviews={["", "", "", "", ""]}
                    defaultRating={rating}
                    isDisabled={true}
                    size={RFValue(25)}
                    starContainerStyle={{ marginTop: -30 }}
                  />
                </View>

                <View style={{ flex: 0.7, padding: 15 }}>
                  <Text style={styles.overview}>{overview}</Text>
                </View>
              </View>
              <View style={styles.lowerBottomContainer}>
                <View style={styles.iconButtonContainer}>
                  <TouchableOpacity onPress = {this.liked_article}>
                    <Icon
                      reverse
                      name={"check"}
                      type={"entypo"}
                      size={RFValue(30)}
                      color={"#76ff03"}
                    />
                  </TouchableOpacity>
                  <TouchableOpacity onPress = {this.unliked_article}>
                    <Icon
                      reverse
                      name={"cross"}
                      type={"entypo"}
                      size={RFValue(30)}
                      color={"#ff1744"}
                    />
                  </TouchableOpacity>
                </View>
                <View style={styles.buttonCotainer}>
                  <TouchableOpacity
                    style={styles.button}
                     onPress = {this.notWatchedMovie}
                    
                  >


const styles = StyleSheet.create({
  container: {
    flex: 1
  },
  headerContainer: {
    flex: 0.1
  },
  headerTitle: {
    color: "#fff",
    fontWeight: "bold",
    fontSize: RFValue(18)
  },
  subContainer: {
    flex: 0.9
  },
  subTopContainer: {
    flex: 0.4,
    justifyContent: "center",
    alignItems: "center"
  },
  posterImage: {
    width: "60%",
    height: "90%",
    resizeMode: "stretch",
    borderRadius: RFValue(30),
    marginHorizontal: RFValue(10)
  },
  subBottomContainer: {
    flex: 0.6
  },
  upperBottomContainer: {
    flex: 0.2,
    alignItems: "center"
  },
  title: {
    fontSize: RFValue(20),
    fontWeight: "bold",
    textAlign: "center"
  },
  subtitle: {
    fontSize: RFValue(14),
    fontWeight: "300"
  },
  middleBottomContainer: {
    flex: 0.35
  },
  overview: {
    fontSize: RFValue(13),
    textAlign: "center",
    fontWeight: "300",
    color: "gray"
  },
  lowerBottomContainer: {
    flex: 0.45
  },
  iconButtonContainer: {
    flexDirection: "row",
    justifyContent: "space-evenly",
    alignItems: "center"
  },
  buttonCotainer: {
    justifyContent: "center",
    alignItems: "center"
  },
  button: {
    width: RFValue(160),
    height: RFValue(50),
    borderRadius: RFValue(20),
    justifyContent: "center",
    alignItems: "center",
    borderWidth: 1,
    marginTop: RFValue(15)
  },
  buttonText: {
    fontSize: RFValue(15),
    fontWeight: "bold"
  }
});
