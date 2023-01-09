import Movie from '../componetes/Movie';
import {useEffect, useState} from "react";
import PropTypes from "prop-types";

function Home(){
    const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  const getMovies = async () => {
    // const json = await response.json(); 
    const json = await(
      await fetch(
        'https://yts.mx/api/v2/list_movies.json?minimum_rating=8.8&sort_by=year'
      )
    ).json();
    setMovies(json.data.movies);
    setLoading(false);
    };
    useEffect(() => {
      getMovies();
    }, []);
    console.log(movies);
  return <div>
    {loading ? 
      <h1>Loading...</h1> : 
      <div>{movies.map(m => 
          <Movie 
            key={m.id}
            id= {m.id}
            mediumCoverImage = {m.medium_cover_image} 
            title = {m.title}
            summary = {m.summary}
            genres = {m.genres}
          />
        )}</div>
    }</div>;
}

Movie.propTypes = {
    id :PropTypes.number.isRequired,
  mediumCoverImage:PropTypes.string.isRequired,
  title:PropTypes.string.isRequired,
  summary:PropTypes.string.isRequired,
  genres:PropTypes.arrayOf(PropTypes.string).isRequired,

}
export default Home;