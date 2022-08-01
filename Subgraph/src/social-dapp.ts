import { Post as PostEvent } from "../generated/SocialDapp/SocialDapp";
import { Post } from "../generated/schema";

export function handlePost(event: PostEvent): void {
  let entity = new Post(event.params.id);
  entity.sender = event.params.sender;
  entity.save();
}
