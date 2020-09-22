module Program

open Pulumi.FSharp
open Pulumi.Aws.S3

let infra () =

  // Create an AWS resource (S3 Bucket)
  let bucket = Bucket "pulumi-fsharp-01"

  // Export the name of the bucket
  dict [("bucketName", bucket.Id :> obj)]

[<EntryPoint>]
let main _ =
  Deployment.run infra
