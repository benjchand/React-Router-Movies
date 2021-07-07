import React, { Component } from 'react';

import SavedList from './Movies/SavedList';
import MovieList from './Movies/MovieList';
import Movie from './Movies/Movie';
import {Route} from 'react-router-dom';

export default class App extends Component {
  constructor() {
    super();
    this.state = {
      savedList: [],
      movieInList: null
    };
  }

  addToSavedList = movie => {
    const savedList = this.state.savedList;
    const findMovie = savedList.find(element => movie.id === element.id);
    if (findMovie) {
      this.setState({ movieInList: `That movie is already saved.` });
      setTimeout(() => this.setState({ movieInList: null }), 2000);
    } else {
      savedList.push(movie);
    }

    this.setState({ savedList });
  };

  render() {
    const { movieInList } = this.state;
    return (
      <div>
        {movieInList !== null ? (
          <h3 className="movie-warning">{movieInList}</h3>
        ) : null}
        <SavedList list={this.state.savedList} />
        <Route exact path="/" component={MovieList} />
        <Route
          path="/movies/:id"
          render={props => (
            <Movie {...props} addToSavedList={this.addToSavedList} />
          )}
        />
      </div>
    );
  }
}