
https://gitlab.hot.com/oauth/authorize?client_id=c21d3ed64ccf09d254c85de25cbf894e4935c9e2412a4b5aef27679150a93563&redirect_uri=http://localhost:8080/oauth/redirect&response_type=code&state=11111111&scope=api

http://localhost:8080/oauth/redirect?code=b99647a3854d040d6e48daa3246308621070f66644a83d267b631a421d109fc4&state=11111111

http://localhost:8080/oauth/redirect?code=b90a04c02b8ad0150967e3cba91ae5b8da01bd67e6d2334ff0d9cc7fb447e4b6&state=11111111

parameters = 'client_id=APP_ID&client_secret=APP_SECRET&code=RETURNED_CODE&grant_type=authorization_code&redirect_uri=REDIRECT_URI'
RestClient.post 'http://gitlab.example.com/oauth/token', parameters

```shell
echo 'client_id=c21d3ed64ccf09d254c85de25cbf894e4935c9e2412a4b5aef27679150a93563&client_secret=3ea3b139fc2ae85154273c7b1a269531c84e41e6dcea3d6ae5444f3ff1eec533&code=b90a04c02b8ad0150967e3cba91ae5b8da01bd67e6d2334ff0d9cc7fb447e4b6&grant_type=authorization_code&redirect_uri=http://localhost:8080/oauth/redirect' > auth.txt
```

```shell
curl --data "@auth.txt" --request POST https://gitlab.hot.com/oauth/token
```

```json
{"access_token":"fb6c634abadce714e8dad55567c7762d101188ceadc74ef771a90035b23dfb8c","token_type":"bearer","refresh_token":"9e977e9a8f33e14a55fc21f1a0bdce204749b52b62e1afa70dc17a30702022c0","scope":"api","created_at":1567826808}
```

```shell
curl --header "Authorization: Bearer fb6c634abadce714e8dad55567c7762d101188ceadc74ef771a90035b23dfb8c" https://gitlab.hot.com/api/v4/user
```

```json
{
	"id": 1063,
	"name": "juzhanglei 00234709",
	"username": "j00234709",
	"state": "active",
	"avatar_url": "https://w3.hot.com/w3lab/rest/yellowpage/face/00234709/120",
	"web_url": "https://gitlab.hot.com/j00234709",
	"created_at": "2018-09-23T18:23:48.809+08:00",
	"bio": null,
	"location": null,
	"public_email": "",
	"skype": "",
	"linkedin": "",
	"twitter": "",
	"website_url": "",
	"organization": null,
	"last_sign_in_at": "2019-08-30T16:27:13.605+08:00",
	"confirmed_at": "2018-09-23T18:23:48.761+08:00",
	"last_activity_on": "2019-09-07",
	"email": "jack.ju@hot.com",
	"theme_id": 1,
	"color_scheme_id": 1,
	"projects_limit": 100000,
	"current_sign_in_at": "2019-09-07T10:11:31.922+08:00",
	"identities": [{
		"provider": "ldapmain",
		"extern_uid": "cn=juzhanglei 00234709,ou=corpusers,dc=china,dc=huawei,dc=com"
	}],
	"can_create_group": true,
	"can_create_project": true,
	"two_factor_enabled": false,
	"external": false,
	"private_profile": null
}
```

```shell
curl --header "Authorization: Bearer fb6c634abadce714e8dad55567c7762d101188ceadc74ef771a90035b23dfb8c" https://gitlab.hot.com/api/v4/groups
```

```json
[{
	"id": 76344,
	"web_url": "https://gitlab.hot.com/groups/Hotbug/Api",
	"name": "Api",
	"path": "Api",
	"description": "",
	"visibility": "private",
	"lfs_enabled": true,
	"avatar_url": null,
	"request_access_enabled": false,
	"full_name": "Hotbug / Api",
	"full_path": "Hotbug/Api",
	"parent_id": 76341
},
{
	"id": 76341,
	"web_url": "https://gitlab.hot.com/groups/Hotbug",
	"name": "Hotbug",
	"path": "Hotbug",
	"description": "",
	"visibility": "private",
	"lfs_enabled": true,
	"avatar_url": null,
	"request_access_enabled": false,
	"full_name": "Hotbug",
	"full_path": "Hotbug",
	"parent_id": null
},
{
	"id": 1400,
	"web_url": "https://gitlab.hot.com/groups/MallBook",
	"name": "MallBook",
	"path": "MallBook",
	"description": "",
	"visibility": "private",
	"lfs_enabled": true,
	"avatar_url": null,
	"request_access_enabled": false,
	"full_name": "MallBook",
	"full_path": "MallBook",
	"parent_id": null
},
{
	"id": 76342,
	"web_url": "https://gitlab.hot.com/groups/Hotbug/Marketing",
	"name": "Marketing",
	"path": "Marketing",
	"description": "",
	"visibility": "private",
	"lfs_enabled": true,
	"avatar_url": null,
	"request_access_enabled": false,
	"full_name": "Hotbug / Marketing",
	"full_path": "Hotbug/Marketing",
	"parent_id": 76341
},
{
	"id": 2358,
	"web_url": "https://gitlab.hot.com/groups/nce_gopkgs",
	"name": "nce_gopkgs",
	"path": "nce_gopkgs",
	"description": "NCE gopkgs group",
	"visibility": "public",
	"lfs_enabled": true,
	"avatar_url": null,
	"request_access_enabled": false,
	"full_name": "nce_gopkgs",
	"full_path": "nce_gopkgs",
	"parent_id": null
},
{
	"id": 76343,
	"web_url": "https://gitlab.hot.com/groups/Hotbug/Services",
	"name": "Services",
	"path": "Services",
	"description": "",
	"visibility": "private",
	"lfs_enabled": true,
	"avatar_url": null,
	"request_access_enabled": false,
	"full_name": "Hotbug / Services",
	"full_path": "Hotbug/Services",
	"parent_id": 76341
}]
```

```shell
curl --header "Authorization: Bearer fb6c634abadce714e8dad55567c7762d101188ceadc74ef771a90035b23dfb8c" https://gitlab.hot.com/api/v4/groups/76344/projects
```

```json
[{
	"id": 42965,
	"description": "",
	"name": "IdeaService",
	"name_with_namespace": "Hotbug / Api / IdeaService",
	"path": "IdeaService",
	"path_with_namespace": "Hotbug/Api/IdeaService",
	"created_at": "2019-09-07T11:34:22.276+08:00",
	"default_branch": "master",
	"tag_list": [],
	"ssh_url_to_repo": "ssh://git@gitlab.hot.com:2222/Hotbug/Api/IdeaService.git",
	"http_url_to_repo": "https://gitlab.hot.com/Hotbug/Api/IdeaService.git",
	"web_url": "https://gitlab.hot.com/Hotbug/Api/IdeaService",
	"readme_url": "https://gitlab.hot.com/Hotbug/Api/IdeaService/blob/master/README.md",
	"avatar_url": null,
	"star_count": 0,
	"forks_count": 0,
	"last_activity_at": "2019-09-07T11:34:22.276+08:00",
	"namespace": {
		"id": 76344,
		"name": "Api",
		"path": "Api",
		"kind": "group",
		"full_path": "Hotbug/Api",
		"parent_id": 76341
	},
	"_links": {
		"self": "https://gitlab.hot.com/api/v4/projects/42965",
		"issues": "https://gitlab.hot.com/api/v4/projects/42965/issues",
		"merge_requests": "https://gitlab.hot.com/api/v4/projects/42965/merge_requests",
		"repo_branches": "https://gitlab.hot.com/api/v4/projects/42965/repository/branches",
		"labels": "https://gitlab.hot.com/api/v4/projects/42965/labels",
		"events": "https://gitlab.hot.com/api/v4/projects/42965/events",
		"members": "https://gitlab.hot.com/api/v4/projects/42965/members"
	},
	"archived": false,
	"visibility": "private",
	"resolve_outdated_diff_discussions": false,
	"container_registry_enabled": true,
	"issues_enabled": true,
	"merge_requests_enabled": true,
	"wiki_enabled": true,
	"jobs_enabled": true,
	"snippets_enabled": true,
	"shared_runners_enabled": false,
	"lfs_enabled": true,
	"creator_id": 1063,
	"import_status": "none",
	"open_issues_count": 0,
	"public_jobs": true,
	"ci_config_path": null,
	"shared_with_groups": [],
	"only_allow_merge_if_pipeline_succeeds": false,
	"request_access_enabled": false,
	"only_allow_merge_if_all_discussions_are_resolved": false,
	"printing_merge_request_link_enabled": true,
	"merge_method": "merge"
}]
```

```shell
curl --header "Authorization: Bearer fb6c634abadce714e8dad55567c7762d101188ceadc74ef771a90035b23dfb8c" https://gitlab.hot.com/api/v4/groups/76344/members/all
```

```json
[{
	"id": 1063,
	"name": "juzhanglei 00234709",
	"username": "j00234709",
	"state": "active",
	"avatar_url": "https://w3.hot.com/w3lab/rest/yellowpage/face/00234709/120",
	"web_url": "https://gitlab.hot.com/j00234709",
	"access_level": 50,
	"expires_at": null
}]
```

```go
h := requests.Header{
	"Authorization": "Bearer " + reqContext.AccessToken,
}
resp, err := requests.Get(url, h)
if err != nil {
	e = types.NewError(requests.StatusInternalServerError, err)
	return
}
if resp.StatusCode != 200 {
	e = types.NewError(resp.StatusCode, errors.New(resp.Text()))
	return
}
fmt.Println(resp)
fmt.Println(resp.Text())
var u user
err = json.Unmarshal(resp.Content(), &u)
if err != nil {
	e = types.NewError(requests.StatusInternalServerError, err)
	return
}
```

