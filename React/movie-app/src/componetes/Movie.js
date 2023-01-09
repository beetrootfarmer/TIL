import {Link} from "react-router-dom";
function Movie({id, mediumCoverImage,title, summary, genres}){
    return(
        <div>
            <img src={mediumCoverImage} alt=""/>
            <h2>
              <Link to={`/movie/${id}`}>{title}</Link>
            </h2>
            <p>{summary}</p>
            <ul>
              {genres.map((g) => (
                <li key={g}>{g}</li>
              ))}
            </ul>
          </div>
    )
}
export default Movie;