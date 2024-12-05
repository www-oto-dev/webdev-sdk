// This file was generated by liblab | https://liblab.com/

package com.swagger.petstore.services;

import com.fasterxml.jackson.core.type.TypeReference;
import com.swagger.petstore.exceptions.ApiException;
import com.swagger.petstore.http.HttpMethod;
import com.swagger.petstore.http.ModelConverter;
import com.swagger.petstore.http.util.RequestBuilder;
import java.util.concurrent.CompletableFuture;
import lombok.NonNull;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

/**
 * V0Service Service
 */
public class V0Service extends BaseService {

  public V0Service(@NonNull OkHttpClient httpClient, String serverUrl) {
    super(httpClient, serverUrl);
  }

  /**
   * Read Root
   *
   * @return response of {@code Object}
   */
  public Object readRootV0AdminGet() throws ApiException {
    Request request = this.buildReadRootV0AdminGetRequest();
    Response response = this.execute(request);
    return ModelConverter.convert(response, new TypeReference<Object>() {});
  }

  /**
   * Read Root
   *
   * @return response of {@code CompletableFuture<Object>}
   */
  public CompletableFuture<Object> readRootV0AdminGetAsync() throws ApiException {
    Request request = this.buildReadRootV0AdminGetRequest();
    CompletableFuture<Response> futureResponse = this.executeAsync(request);
    return futureResponse.thenApplyAsync(response -> ModelConverter.convert(response, new TypeReference<Object>() {}));
  }

  private Request buildReadRootV0AdminGetRequest() {
    return new RequestBuilder(HttpMethod.GET, this.serverUrl, "v0/admin/").build();
  }

  /**
   * Read Root
   *
   * @return response of {@code Object}
   */
  public Object readRootV0AdminProjectsGet() throws ApiException {
    Request request = this.buildReadRootV0AdminProjectsGetRequest();
    Response response = this.execute(request);
    return ModelConverter.convert(response, new TypeReference<Object>() {});
  }

  /**
   * Read Root
   *
   * @return response of {@code CompletableFuture<Object>}
   */
  public CompletableFuture<Object> readRootV0AdminProjectsGetAsync() throws ApiException {
    Request request = this.buildReadRootV0AdminProjectsGetRequest();
    CompletableFuture<Response> futureResponse = this.executeAsync(request);
    return futureResponse.thenApplyAsync(response -> ModelConverter.convert(response, new TypeReference<Object>() {}));
  }

  private Request buildReadRootV0AdminProjectsGetRequest() {
    return new RequestBuilder(HttpMethod.GET, this.serverUrl, "v0/admin/projects").build();
  }

  /**
   * Read Root
   *
   * @return response of {@code Object}
   */
  public Object readRootV0ControlGet() throws ApiException {
    Request request = this.buildReadRootV0ControlGetRequest();
    Response response = this.execute(request);
    return ModelConverter.convert(response, new TypeReference<Object>() {});
  }

  /**
   * Read Root
   *
   * @return response of {@code CompletableFuture<Object>}
   */
  public CompletableFuture<Object> readRootV0ControlGetAsync() throws ApiException {
    Request request = this.buildReadRootV0ControlGetRequest();
    CompletableFuture<Response> futureResponse = this.executeAsync(request);
    return futureResponse.thenApplyAsync(response -> ModelConverter.convert(response, new TypeReference<Object>() {}));
  }

  private Request buildReadRootV0ControlGetRequest() {
    return new RequestBuilder(HttpMethod.GET, this.serverUrl, "v0/control/").build();
  }

  /**
   * Read Root
   *
   * @return response of {@code Object}
   */
  public Object readRootV0ControlProjectsGet() throws ApiException {
    Request request = this.buildReadRootV0ControlProjectsGetRequest();
    Response response = this.execute(request);
    return ModelConverter.convert(response, new TypeReference<Object>() {});
  }

  /**
   * Read Root
   *
   * @return response of {@code CompletableFuture<Object>}
   */
  public CompletableFuture<Object> readRootV0ControlProjectsGetAsync() throws ApiException {
    Request request = this.buildReadRootV0ControlProjectsGetRequest();
    CompletableFuture<Response> futureResponse = this.executeAsync(request);
    return futureResponse.thenApplyAsync(response -> ModelConverter.convert(response, new TypeReference<Object>() {}));
  }

  private Request buildReadRootV0ControlProjectsGetRequest() {
    return new RequestBuilder(HttpMethod.GET, this.serverUrl, "v0/control/projects").build();
  }

  /**
   * Read Root
   *
   * @return response of {@code Object}
   */
  public Object readRootV0ProjectGet() throws ApiException {
    Request request = this.buildReadRootV0ProjectGetRequest();
    Response response = this.execute(request);
    return ModelConverter.convert(response, new TypeReference<Object>() {});
  }

  /**
   * Read Root
   *
   * @return response of {@code CompletableFuture<Object>}
   */
  public CompletableFuture<Object> readRootV0ProjectGetAsync() throws ApiException {
    Request request = this.buildReadRootV0ProjectGetRequest();
    CompletableFuture<Response> futureResponse = this.executeAsync(request);
    return futureResponse.thenApplyAsync(response -> ModelConverter.convert(response, new TypeReference<Object>() {}));
  }

  private Request buildReadRootV0ProjectGetRequest() {
    return new RequestBuilder(HttpMethod.GET, this.serverUrl, "v0/project/").build();
  }

  /**
   * Read Root
   *
   * @return response of {@code Object}
   */
  public Object readRootV0ProjectproperiesSetPut() throws ApiException {
    Request request = this.buildReadRootV0ProjectproperiesSetPutRequest();
    Response response = this.execute(request);
    return ModelConverter.convert(response, new TypeReference<Object>() {});
  }

  /**
   * Read Root
   *
   * @return response of {@code CompletableFuture<Object>}
   */
  public CompletableFuture<Object> readRootV0ProjectproperiesSetPutAsync() throws ApiException {
    Request request = this.buildReadRootV0ProjectproperiesSetPutRequest();
    CompletableFuture<Response> futureResponse = this.executeAsync(request);
    return futureResponse.thenApplyAsync(response -> ModelConverter.convert(response, new TypeReference<Object>() {}));
  }

  private Request buildReadRootV0ProjectproperiesSetPutRequest() {
    return new RequestBuilder(HttpMethod.PUT, this.serverUrl, "v0/projectproperies/set").build();
  }
}
